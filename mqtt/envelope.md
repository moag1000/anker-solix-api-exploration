> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# MQTT envelope

This page owns everything that every product shares on the MQTT wire: the JSON `head` and `payload` of a command, the `MqttCommandType` values that go into `head.cmd`, the topic strings, the gzip check, the binary frame inside `payload.data` and the TLV field layout inside that frame. Per-product field maps (tags, names, scales) live on the `mqtt/<pn>.md` pages, for example [a17c1.md](a17c1.md) and [a17x8.md](a17x8.md).

Evidence for every value is a row of the Smi audit [../docs/audit/BLE_COMMAND_MAP.md](../docs/audit/BLE_COMMAND_MAP.md) (written `audit row N` below) plus the asm address that row carries (`file.dart @0xADDR`, 3.24.3 unless stated). Integers follow the Smi rule in [../METHODOLOGY.md](../METHODOLOGY.md#smi-rule-reading-numbers-from-blutter-output): a raw immediate stored with `stur w` is halved, so the values below are the real wire values and differ from the raw numbers of the superseded `BLE_COMMAND_MAP.md`. Where the app and upstream agree the cell also says `upstream-confirmed` with the `anker-solix-api` line; upstream names win.

Not here: the BLE side of the same frame (MTU split, handshake) is in `ble/protocol.md` (audit rows 45-62 belong there); endpoint payloads are in [../api/README.md](../api/README.md).

## Contents

1. [Layers at a glance](#layers-at-a-glance)
1. [Head fields](#head-fields)
1. [Command types](#command-types)
1. [Payload variants](#payload-variants)
1. [Topics](#topics)
1. [Receive path and gzip](#receive-path-and-gzip)
1. [Binary layer](#binary-layer)
1. [TLV frame](#tlv-frame)
1. [Data type codes](#data-type-codes)
1. [intToList encodings](#inttolist-encodings)
1. [Direction detection](#direction-detection)
1. [Connection details](#connection-details)
1. [Infrastructure](#infrastructure)
1. [Since 3.18.0](#since-3180)
1. [Known unknowns](#known-unknowns)

## Layers at a glance

A command is a JSON object published to a `.../req` topic. `payload` carries `data`, a base64 string. The decoded bytes are one binary frame: a 9-byte header, TLV fields, an XOR byte. The field tags (`a2`, `a3`, ...) and their meaning depend on the product number and the 2-byte opcode, and are documented per product.

```text
JSON  { head{...}, payload{ device_sn, account_id, data=base64 } }
data  FF 09 | len(2) | 03 00 0F | opcode(2) | A1 01 22 | tag len type data ... | FE/FD trailer | xor
```

The line above is a layout sketch, not a capture. Tag: asm-traced (details in the sections below).

## Head fields

Built by `MqttCommandTransformer.generateCommand` (`charging/communication/transformer/mqtt_command_transformer.dart`).

| field | value the app sends | type | source |
|---|---|---|---|
| `version` | not audited for the app; upstream sends `"1.0.0.1"` | string | upstream-confirmed (`api/mqtt.py` line 372) |
| `client_id` | not audited for the app; upstream sends `android-<app_name>-<user_id>-<certificate_id>` | string | upstream-confirmed (`api/mqtt.py` line 373) |
| `sess_id` | `"1"` (upstream default `"1234-5678"`, lines 360 and 374) | string | audit row 26, audit row 64; generateCommand @0x226ef1c (pool string [pp+0xede8]) |
| `msg_seq` | 1 (raw immediate is 2, stored with `stur w`) | int | audit row 27, audit row 65; generateCommand @0x226ef34; upstream-confirmed (`api/mqtt.py` line 375) |
| `cmd` | the `cmdMap` lookup result for the `MqttCommandType`, see [Command types](#command-types) | int | audit row 28; cmdMap @0x226f2a4 |
| `cmd_status` | 2 (raw 4) | int | audit row 29; generateCommand @0x226ef94; upstream-confirmed (`api/mqtt.py` line 380) |
| `sign_code` | 1 (raw 2) | int | audit row 30; generateCommand @0x226efa8; upstream-confirmed (`api/mqtt.py` line 382) |
| `seed` | `"1"` (upstream: `1`, or 16 random bytes as hex when an `encoding_type` is given, lines 376-378) | string | audit row 26; generateCommand @0x226efbc |
| `timestamp` | Unix epoch seconds written at send time (`getCurrentTimestamp`: two divisions by 1000) | int | audit row 22 @0x226edb0..0x226edbc; audit row 31 (the example value in the old doc is not from asm) |
| `device_pn`, `device_sn` | product number and serial of the target | string | upstream-confirmed (`api/mqtt.py` lines 383-387) |

The superseded doc listed `cmd_status` 4, `sign_code` 2, `msg_seq` 2 (and the head value 34 for `normalCommand`): all were raw Smi immediates (audit rows 28-30, 65). Example with placeholders instead of numbers that belong to the command-type table:

synthesized

```text
head:    version, client_id, sess_id="1", msg_seq=1, seed="1", timestamp=<now, s>,
         cmd_status=2, cmd=<value from the command type table>, sign_code=1, device_pn, device_sn
payload: device_sn, account_id, data=<base64 frame>
```

## Command types

`cmdMap` is a `Map<MqttCommandType, int>` literal built at @0x226f274; each value is a tagged Smi stored with `stur w16`, so real value = raw / 2 (audit rows 32-40, same raw immediates at the 3.18.0 sites). The head value is read with `LoadInt32Instr` and written into the head.

| MqttCommandType | head value (dec) | hex | raw immediate | enum index | source |
|---|---|---|---|---|---|
| `normalCommand` | 17 | 0x11 | 34 | 0 | audit row 32; cmdMap @0x226f2a4; index: audit row 41; upstream-confirmed (`api/mqtt.py` line 359, default of `publish`) |
| `otaCommand` | 6 | 0x06 | 12 | 1 | audit row 33; cmdMap @0x226f2b8; index: audit row 35 [pp+0x137a8] |
| `a17y0OtaCommand` | 6 | 0x06 | 12 | 2 | audit row 34; cmdMap @0x226f2cc; index: audit row 35 [pp+0x137b0] |
| `uploadLogCommand` | 5 | 0x05 | 10 | 4 | audit row 36; cmdMap @0x226f2e0; index: audit row 43 |
| `remoteScanWifi` | 25 | 0x19 | 50 | 5 | audit row 37; cmdMap @0x226f2f4; index: audit row 44 |
| `remoteSwitchWifi` | 26 | 0x1A | 52 | 6 | audit row 38; cmdMap @0x226f308; index: audit row 44 |
| `unbindDevice` | 12 | 0x0C | 24 | not audited | audit row 39; cmdMap @0x226f31c |
| `getDeviceBssid` | 28 | 0x1C | 56 | not audited | audit row 40; cmdMap @0x226f330 |

`otaCommand` and `a17y0OtaCommand` map to the same head value; the duplicate is real, only the old doc's value was doubled (audit row 35). Only the `normalCommand` value has upstream confirmation. Ordinary product commands (everything on the `mqtt/<pn>.md` pages) use `normalCommand`.

## Payload variants

`generateCommand` branches on the unboxed enum index (`cmp x3,#N`, audit rows 41-44). All variants carry `device_sn` and `account_id` (upstream-confirmed, `api/mqtt.py` lines 390-395).

| enum index | MqttCommandType | extra payload fields | source |
|---|---|---|---|
| 0 | `normalCommand` | `data`: base64 of the binary frame | audit row 41; generateCommand @0x226e964, @0x226e96c; upstream-confirmed (`api/mqtt.py` line 395) |
| 1 | `otaCommand` | none | audit row 42; branch @0x226e9c8 (the old doc attached the OTA field to this member by mistake) |
| 2 | `a17y0OtaCommand` | `ota_type` = `"A17Y0"` | audit row 42; generateCommand @0x226e9c8 |
| 4 | `uploadLogCommand` | `log_id` = device_sn + `" "` + timestamp | audit row 43; generateCommand @0x226ea00, @0x226ea08 (separator @0x226ece4) |
| 5 | `remoteScanWifi` | none | audit row 44; branch compare @0x226ea4c |
| 6 | `remoteSwitchWifi` | `ssid`, `pwd`, `timezone`, `timeid` | audit row 44; generateCommand @0x226ea4c, @0x226ea68 |

There is no `wifiConfig` member (audit row 44). Upstream can add `encoding_type` to the payload (`api/mqtt.py` lines 399-402, upstream-confirmed); the app side of that field was not found (audit row 315 searched `encoding_type` in `ev_charger/` and `pp.txt`, no hit).

## Topics

All topics are built in `charging/mqtt/business/mqtt_serve.dart`. `getCommonTopicString` @0x2206dc8 interpolates five parts: the literal `anker_power`, `/`, a getter result, `/`, a second getter result (array length raw 10 = 5 elements, audit Smi rule). Upstream builds the same string as `<cmd|dt>/<app_name>/<pn>/<sn>/` with the product number first and the serial second (`api/mqtt.py` lines 315-329, upstream-confirmed); that binding of the two getters is therefore `upstream-confirmed`, the literals below are asm-traced.

| direction | pattern | source |
|---|---|---|
| publish (commands) | `cmd/anker_power/<pn>/<sn>/req` | mqtt_serve.dart @0x226fac4..0x226fb08; upstream-confirmed (`api/mqtt.py` line 408) |
| subscribe (command response) | `cmd/anker_power/<pn>/<sn>/app/res` | mqtt_serve.dart @0x2206d5c..0x2206da0 |
| subscribe (basic info) | `dt/anker_power/<pn>/<sn>/basic_info` | mqtt_serve.dart @0x2207cf8..0x2207d3c |
| subscribe (parameter info, the 0405 family) | `dt/anker_power/<pn>/<sn>/param_info` | mqtt_serve.dart @0x2207de0..0x2207e24; upstream-confirmed (TOPIC `param_info` in `api/mqttmap.py`, for example line 1798) |
| subscribe (state info, the 0408 family) | `dt/anker_power/<pn>/<sn>/state_info` | mqtt_serve.dart @0x3b59c84..0x3b59cc8; upstream-confirmed (`api/mqttmap.py` line 1867) |
| other topics found | `cmd/anker_power/<pn>/<sn>/res` @0x2447e30..0x2447e70, `dt/anker_power/<pn>/<sn>/power_site` @0x2359f7c..0x2359fbc and the fixed literal `cmd/anker_power/anonymous/req` @0x2447c0c (pool string [pp+0x2dac0]) | mqtt_serve.dart (asm-traced literal and site; payload not documented) |

Upstream extracts the model and serial of a received message from topic segments 2 and 3 (`api/mqtt.py` lines 136-139, upstream-confirmed). The old doc listed only four topics; `state_info`, `res`, `power_site` and the anonymous literal were not in it.

## Receive path and gzip

`MqttDecompressionUtil.decompressPayload` checks the first two bytes for the gzip magic before decoding (audit row 25): byte 0 equals 0x1F @0x2863ccc and byte 1 equals 0x8B @0x2863ce8, both compared as unboxed bytes (real values). Bytes without the magic are used unchanged. Which bytes are fed to this function (the whole MQTT body or the base64-decoded `data` field) is not established by the audit, see [Known unknowns](#known-unknowns). Upstream decodes the MQTT body as UTF-8 JSON and base64-decodes `payload.data` (or `payload.trans` for JSON devices) with no gzip step (`api/mqtt.py` lines 124-147, upstream-confirmed).

## Binary layer

Built by `ZXCommandTransformer._getNormalCommand` (`charging/communication/transformer/zx_command_transformer.dart`).

| byte offset | value | meaning | source |
|---|---|---|---|
| 0-1 | `FF 09` | frame marker, pool list `const [0xff, 0x9]` | audit row 4; @0x2274320 |
| 2-3 | length, 16-bit little endian | total length including the header; the header is 9 bytes (`add x0,x1,#9`) | audit row 4 @0x22742a8; upstream-confirmed (`api/mqtttypes.py` lines 39-45: the length includes prefix and the XOR byte) |
| 4 | `03` | constant (raw immediate 6, halved) | audit row 5; @0x2274368 |
| 5 | `00` | the app writes the zero register; the receive variant `01` was not found in the app | audit row 6; @0x22743b8; upstream-confirmed (`api/mqtttypes.py` line 42, `03 00/01 0f` for send and receive) |
| 6 | `0F` in captures | loaded from transformer field `field_23`, value unresolved | audit row 6; @0x22743f8; upstream-confirmed (`api/mqtttypes.py` line 82) |
| 7-8 | opcode as written in the Dart hex string, for example `00 7A` for `"007a"` | pool lists such as `[0, 0x7a]` are the same two bytes in order | audit row 165 (pool list `[0, 0x5e]`), audit row 167; byte order on the wire: upstream-confirmed (`api/mqtttypes.py` line 43, `04 05` for status `0405`) |
| last | XOR of all preceding bytes, start value 0 | checksum, included in the length | audit row 14 (address corrected 2026-10-19, see ble/protocol.md): ZXCmdUtil.getCheckSum `ak_cmd_util.dart` @0x2272e9c (start value @0x2272e2c); send side ZXCommandTransformer._getCheckSum `zx_command_transformer.dart` @0x22745f0 (eor @0x227463c, called @0x2274518). The audit's @0x22744a4 is the `eor` that folds the 0x40 encrypted flag into opcode byte 0, not the checksum |

An optional increment byte after the opcode appears on some upstream-observed messages (`api/mqtttypes.py` line 44); the app side was not audited.

## TLV frame

Generic single-value builder: `_getSettingCommand` (same file), used by every setter that sends one tag; multi-tag setters build their own map and share the head fields.

| position | value | meaning | source |
|---|---|---|---|
| first field | `A1 01 22` (set) or `A1 01 21` (clear) | tag A1, length 1, value 0x22 or 0x21; a bool transformer field selects 0x22 (set) or 0x21. The old doc called the second byte a protocol version (`02`) and the third a direction (`42`/`44`); both were raw Smi values | audit row 7 @0x2273568 (raw 322 = 0xA1); audit row 8 @0x22735ac (raw 2 = 1); audit row 9 @0x2273510 (raw 0x42/0x44 = 0x21/0x22); upstream-confirmed (`api/mqttcmdmap.py` line 212, `pattern_22`) |
| field tag | `A2` for the single-value form | key raw 324, halved | audit row 10; @0x22736f8 |
| field length | payload length + 1, one byte; two bytes (`intToList2`) only when the transformer flag `field_33` is set | the +1 counts the type byte | audit row 11; @0x2273978, @0x2273710 |
| type byte | data type code, see [Data type codes](#data-type-codes) | derived from the value length | audit row 12; @0x2273738 |
| data | value bytes, little endian | `intToList*` | audit row 21 @0x2272ec8 |
| timestamp trailer | tag `FE`, 4 bytes little endian seconds (`intToList4` of `getCurrentTimestamp`) | classic format | audit row 13 @0x2273bc0, @0x2273c90 (key raw 508 = 0xFE); audit row 23 |
| CRC trailer | tag `FD`, 4 bytes: CRC32 of the payload | newer format (A17C1 builders), NOT a millisecond timestamp | audit row 24 @0x281aa44..0x281aa94 (setBackPower), @0x288b224..0x288b238 (setTacticsTime); key raw 506 = 0xFD; audit row 219 |
| checksum | XOR byte | see Binary layer | audit row 14; `_getCheckSum` @0x22745f0 (address corrected, see Binary layer) |

With a one-byte length the type byte sits at field offset 2, with a two-byte length at offset 3 (audit row 12). Disagreement with upstream, recorded rather than resolved: upstream describes tag `fd` as a timestamp in milliseconds sent as a string (`api/mqttcmdmap.py` lines 163-169, TIMESTAMP_FD) and `fe` as a 4-byte value (lines 172-178). The app builders write a CRC32 under 0xFD. Both statements stand side by side; whether a device accepts either form under tag 0xFD is untested in this repo.

A worked synthesized frame (a `007a` switch-on) is kept once, on [a17x8.md](a17x8.md#007a-setrelayswitchcmd), built from these rules; no example in this repo is a capture.

## Data type codes

`_getDataType` @0x2273f20 maps the length of the value list to the type byte (audit rows 16-19); the code is then passed to `intToList`.

| code | upstream name (`DeviceHexDataTypes`) | the app produces it when | source |
|---|---|---|---|
| 1 | `ui` (1 byte, unsigned) | value list length is 1 | audit row 16 @0x2273f64; upstream-confirmed (`api/apitypes.py` line 2132) |
| 2 | `sile` (2 bytes, signed little endian) | value list length is 2; "signed" is not visible in asm | audit row 17 @0x2273f74; upstream-confirmed (`api/apitypes.py` line 2133) |
| 3 | `var` | value list length is exactly 4 (not "1-4 bytes" as the old doc said) | audit row 18 @0x2273f84; upstream-confirmed (`api/apitypes.py` line 2136) |
| 4 | `bin` | every other length, for example 3 | audit row 19 @0x2273f94; upstream-confirmed (`api/apitypes.py` line 2140) |
| 0 | `str` | never produced by this function | audit row 20 (searched `_getDataType` and its inlined copies); upstream-confirmed (`api/apitypes.py` line 2131) |
| 5 | `sfle` (4 bytes, signed float) | never produced by this function | audit row 20; upstream-confirmed (`api/apitypes.py` line 2141) |

Codes 0 and 5 are therefore receive-side types known from upstream only. Scale factors (x0.1, x0.01) and the `listToInt` byte order are owned by `ble/protocol.md`.

## intToList encodings

| function | result | source |
|---|---|---|
| `intToList(value)` | 1 byte | audit row 2; a17x8_device_controller.dart setCountdownCmd @0x3dcfbe4, @0x3dcfdf0 |
| `intToList2(value)` | `[value & 0xFF, (value >> 8) & 0xFF]`, little endian | audit row 21; cmd_util.dart CmdUtil.intToList2 @0x2272ec8 |
| `intToList3(value)` | 3 bytes | audit row 2; setCountdownCmd @0x3dcfbe4 |
| `intToList4(value)` | 4 bytes, same pattern | audit row 21 @0x2272ec8 |
| `getCurrentTimestamp()` | microseconds since epoch divided by 1000 twice = seconds | audit row 22 @0x226edb0..0x226edbc |

The type byte is derived from the byte length of these lists, not from the function name (audit row 2): a 3-byte value gets type 4.

## Direction detection

`ZXCmdUtil.isResponseOrRequest` @0x241fed8 tests `(byte[0] & 0x0F) >> 3 & 1` on unboxed bytes (`and w2,w1,#0xf; lsr w1,w2,#3; and w2,w1,#1; cmp w2,#1`): 0 is a request, 1 a response (audit row 15; byte index 0 is the zero register).

## Connection details

| item | value | source |
|---|---|---|
| default QoS | atLeastOnce, enum value 1 (atMostOnce 0, exactlyOnce 2) | audit row 63; mqtt_serve.dart @0x226fa40, @0x2447b74, @0x2447c28, @0x2447cd8 (pool enum objects, untagged) |
| `sess_id` and `msg_seq` | constants, so they cannot correlate requests and responses | audit rows 64, 65; generateCommand @0x226ef1c, @0x226ef34 |

The client-side debounce key `"pps_parse_common_" + deviceSn` is a string with no wire value (audit row 66, not carried).

## Infrastructure

Two of these three files are new in 3.24.3 (`i_mqtt_serve.dart` and `mqtt_types.dart` are absent from the 3.18.0 asm tree; `local.dart` exists in both versions). A `find` for `*mqtt*` file names gives 35 files in 3.24.3 against 33 in 3.18.0. The audit has no row for these files; the facts below are new asm reads (class headers, pool objects and the function table of each file) and carry no audit row. The other MQTT infrastructure files (`mqtt_server.dart`, `mqtt_command_transformer.dart`, `mqtt_serve.dart`, `mqtt_decompression_util.dart`) are the sources of the sections above.

| file | role | source |
|---|---|---|
| `base_service/services/i_mqtt_serve.dart` | `abstract class IMqttServe` with no members: the interface that `MqttServe` (`charging/mqtt/business/mqtt_serve.dart`) declares with `implements IMqttServe`; other code obtains the service through the type argument `<IMqttServe>` | class header (`i_mqtt_serve.dart` line 8, class id 6341); `mqtt_serve.dart` class header line 9; type argument [pp+0xcd18] used in `boostrap_impl.dart` @0x49e01d0 and `sync_wifi_logic.dart` @0x34b7dbc |
| `base_service/services/mqtt_types.dart` | `enum MqttTopicSubscriptionStatus` with the values `doesNotExist` (0), `pending` (1) and `active` (2); the type `Map<MqttTopicSubscriptionStatus, String>` appears in `MqttServe` and `SdkImpMqttManager` | class header (`mqtt_types.dart` line 8, class id 17160); pool objects [pp+0x11e68] (0), [pp+0x33d30] (1), [pp+0x33d40] (2); `_enumToString` @0x472fdac; map type [pp+0xcca0] in `sdk_imp_mqtt_manager.dart` |
| `charging/mqtt/local.dart` | not a local-network MQTT client: an `abstract class Certificates` with the accessors `ci()` @0x2408a9c, `mp()` @0x2408c90 and `rootCA()` @0x24094e8, and the classes `CI` @0x2408adc, `MP` @0x2408cd0, `UsMp` @0x2408d6c and `EuMp` @0x2408f20 that each build a PEM private key and a PEM certificate from base64 literals (rootCA: one PEM certificate); the material is not reproduced in this repository | constructor and accessor addresses from the asm function table of `local.dart`; the literals are pool strings |

The old controller pointer called `local.dart` "local MQTT"; the file contains certificate and key material only, and the 3.18.0 copy has the same five classes and the same length (687 lines). No reference to `mqtt/local.dart` or to the three accessors was found outside the file itself (grep over the 3.24.3 asm tree), so which of the four certificate sets the app uses for which region or broker is not known.

## Since 3.18.0

The head immediates and the `cmdMap` immediates are the same raw values at the 3.18.0 sites (audit rows 27-30 and 32-40 list both addresses). The gzip check, `_getDataType` and the frame builders are cited for 3.24.3 only; no change was seen by the audit. New in 3.24.3 compared with the old doc's topic list: the `state_info` topic (the audit has no 3.18.0 address for it).

## Known unknowns

- Data type codes 0 (`str`) and 5 (`sfle`) are never produced by `_getDataType` (audit row 20, UNVERIFIABLE; searched the function and its inlined copies); they are known from upstream only.
- Whether the app sends `encoding_type` at all: the audit searched `pp.txt` and `ev_charger/` for it without a hit (audit row 315, UNVERIFIABLE).
- Byte 5 value `01` (receive variant) and the source of byte 6 (`field_23`) were not found (audit row 6).
- Where `decompressPayload` is applied (whole MQTT body or `data` field) is open; upstream shows no gzip step.
- `version` and `client_id` values the APK itself sends were not audited.
- The enum indices of `unbindDevice` and `getDeviceBssid`, and what enum index 3 is, are not in the audit.
- Whether a device accepts a millisecond timestamp under tag 0xFD (as upstream describes) is untested here.
- The old doc's claim that sequence numbers are not used for correlation (it says correlation is topic plus serial) has no audit row; only the constants themselves are traced.
- The product-key and serial getters of `getCommonTopicString` are bound to `<pn>` and `<sn>` by upstream only.
- Which certificate set of `local.dart` (`CI`, `MP`, `UsMp`, `EuMp`, `rootCA`) is used for which broker or region: no caller was found (see Infrastructure).
