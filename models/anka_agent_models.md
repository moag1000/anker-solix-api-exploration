> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Anka AI assistant models

## Contents

1. [AnkaAgentEntryConfigModel](#ankaagententryconfigmodel)
2. [SettingImageModel](#settingimagemodel)
3. [BubbleConfig](#bubbleconfig)
4. [AnkaAgentMenuConfigModel](#ankaagentmenuconfigmodel)
5. [BillAnalysisEntry](#billanalysisentry)
6. [MenuItem](#menuitem)
7. [SubItem](#subitem)
8. [GetSettingResponse](#getsettingresponse)
9. [WelcomeGreetingModel](#welcomegreetingmodel)
10. [ProactiveCtaResponse](#proactivectaresponse)
11. [ProactiveCtaItem](#proactivectaitem)
12. [QuestionBankResponse](#questionbankresponse)

## Purpose

Carries the answers of the Anka AI assistant backend (`smart_service`): the entry configuration (switches, bubble, proactive message, setting images), the menu configuration, the user setting, the welcome greeting, and the question lists (proactive and welcome call-to-action, question bank).

## Dart class + file

`AnkaAgentEntryConfigModel` (`anka_agent/bean/anka_agent_entry_config_model.dart`); `SettingImageModel` (`anka_agent/bean/anka_agent_entry_config_model.dart`); `BubbleConfig` (`anka_agent/bean/bubble_config_model.dart`); `AnkaAgentMenuConfigModel` (`anka_agent/bean/anka_agent_menu_config_model.dart`); `BillAnalysisEntry` (`anka_agent/bean/anka_agent_menu_config_model.dart`); `MenuItem` (`anka_agent/bean/anka_agent_menu_config_model.dart`); `SubItem` (`anka_agent/bean/anka_agent_menu_config_model.dart`); `GetSettingResponse` (`anka_agent/bean/memory_consent_model.dart`); `WelcomeGreetingModel` (`anka_agent/bean/welcome_greeting_model.dart`); `ProactiveCtaResponse` (`anka_agent/pages/home/models/proactive_cta_response_model.dart`); `ProactiveCtaItem` (`anka_agent/pages/home/models/proactive_cta_response_model.dart`); `QuestionBankResponse` (`anka_agent/pages/home/models/question_bank_response_model.dart`). `fromJson` addresses are under each class below.

## Fields

Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Dart types and nullability come from `tools/model_fields.py` (`data/models.json`); an "of `X`" note is the list element class read from the `<X>` type argument next to the key.

### AnkaAgentEntryConfigModel

Answer of `get_all_config` (3.18.0: `get_entry_config`): whether the Anka entry is shown, the agent domain, the switches and the bubble configuration.

`fromJson` `anka_agent_entry_config_model.dart @0x27372c0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `show` | `bool` | yes | ≤3.18.0 | `anka_agent_entry_config_model.dart @0x27372ec` |
| `domain` | `String` | yes | ≤3.18.0 | `anka_agent_entry_config_model.dart @0x2737374` |
| `key_exchange_domain` | `String` | yes | ≤3.18.0 | `anka_agent_entry_config_model.dart @0x2737400` |
| `setting_switch` | `bool?` | yes | ≤3.18.0 | `anka_agent_entry_config_model.dart @0x2737490` |
| `enable` | `bool?` | yes | ≤3.18.0 | `anka_agent_entry_config_model.dart @0x273750c` |
| `setting_images` | `List` of `SettingImageModel` | no | ≤3.18.0 | `anka_agent_entry_config_model.dart @0x273757c` |
| `has_proactive_message` | `bool` | yes | 3.24.3 | `anka_agent_entry_config_model.dart @0x27376a8` |
| `proactive_message_expire_time` | `int?` | yes | 3.24.3 | `anka_agent_entry_config_model.dart @0x2737734` |
| `proactive_message_push_switch` | `int?` | yes | 3.24.3 | `anka_agent_entry_config_model.dart @0x27377ac` |
| `proactive_message_id` | `String?` | yes | 3.24.3 | `anka_agent_entry_config_model.dart @0x2737848` |
| `memory_switch` | `int?` | yes | 3.24.3 | `anka_agent_entry_config_model.dart @0x27378c4` |
| `bill_analysis_switch` | `int?` | yes | 3.24.3 | `anka_agent_entry_config_model.dart @0x273795c` |
| `bill_analysis_show` | `bool?` | yes | 3.24.3 | `anka_agent_entry_config_model.dart @0x27379f4` |
| `power_outage_switch` | `int?` | yes | 3.24.3 | `anka_agent_entry_config_model.dart @0x2737a84` |
| `bubble_config` | `BubbleConfig` | no | 3.24.3 | `anka_agent_entry_config_model.dart @0x2737b20` |

### SettingImageModel

One setting image (function description and image URL) in `setting_images`.

`fromJson` `anka_agent_entry_config_model.dart @0x2737eec`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `function_description` | `String?` | yes | ≤3.18.0 | `anka_agent_entry_config_model.dart @0x2737f1c` |
| `image_url` | `String?` | yes | ≤3.18.0 | `anka_agent_entry_config_model.dart @0x2737f98` |

### BubbleConfig

The bubble the entry button should show (`bubble_config` of the entry configuration); `set_bubble_status` reports it back.

`fromJson` `bubble_config_model.dart @0x2737c28`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `has_bubble` | `bool` | yes | 3.24.3 | `bubble_config_model.dart @0x2737c54` |
| `bubble_type` | `String` | yes | 3.24.3 | `bubble_config_model.dart @0x2737cdc` |
| `bubble_id` | `String` | yes | 3.24.3 | `bubble_config_model.dart @0x2737d68` |
| `bubble_text` | `String` | yes | 3.24.3 | `bubble_config_model.dart @0x2737df4` |

### AnkaAgentMenuConfigModel

Answer of `get_menu_config`: the menu list and the bill-analysis entry.

`fromJson` `anka_agent_menu_config_model.dart @0x35c5468`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `menu_list` | `List` of `MenuItem` | no | ≤3.18.0 | `anka_agent_menu_config_model.dart @0x35c549c` |
| `bill_analysis_entry` | `BillAnalysisEntry?` | yes | 3.24.3 | `anka_agent_menu_config_model.dart @0x35c55b4` |

### BillAnalysisEntry

Bill-analysis entry state inside the menu configuration.

`fromJson` `anka_agent_menu_config_model.dart @0x35c5b14`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `show` | `bool?` | yes | 3.24.3 | `anka_agent_menu_config_model.dart @0x35c5b5c` |
| `privacy_agreed` | `bool?` | yes | 3.24.3 | `anka_agent_menu_config_model.dart @0x35c5bd0` |

### MenuItem

One menu item with sub items.

`fromJson` `anka_agent_menu_config_model.dart @0x35c5cc0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `id` | `int?` | yes | ≤3.18.0 | `anka_agent_menu_config_model.dart @0x35c5cf4` |
| `title` | `String?` | yes | ≤3.18.0 | `anka_agent_menu_config_model.dart @0x35c5d54` |
| `sub_items` | `List` of `SubItem` | no | ≤3.18.0 | `anka_agent_menu_config_model.dart @0x35c5db4` |

### SubItem

One sub item of a menu item.

`fromJson` `anka_agent_menu_config_model.dart @0x35c5f44`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `id` | `int?` | yes | ≤3.18.0 | `anka_agent_menu_config_model.dart @0x35c5f78` |
| `title` | `String?` | yes | ≤3.18.0 | `anka_agent_menu_config_model.dart @0x35c5fd8` |

### GetSettingResponse

Answer of `setting`: the user's proactive, power-outage and memory switches and whether memory exists.

`fromJson` `memory_consent_model.dart @0x364e620`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `proactive_switch` | `int?` | yes | 3.24.3 | `memory_consent_model.dart @0x364e64c` |
| `power_outage_switch` | `int?` | yes | 3.24.3 | `memory_consent_model.dart @0x364e6e4` |
| `memory_switch` | `int?` | yes | 3.24.3 | `memory_consent_model.dart @0x364e77c` |
| `has_memory` | `int?` | yes | 3.24.3 | `memory_consent_model.dart @0x364e814` |

### WelcomeGreetingModel

Answer of `welcome`: the greeting text and the site selection data.

`fromJson` `welcome_greeting_model.dart @0x35c74f8`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `welcome_type` | `String?` | yes | 3.24.3 | `welcome_greeting_model.dart @0x35c7524` |
| `content` | `String?` | yes | 3.24.3 | `welcome_greeting_model.dart @0x35c75a4` |
| `site_count` | `int?` | yes | 3.24.3 | `welcome_greeting_model.dart @0x35c7620` |
| `site_ids_str` | `String?` | yes | 3.24.3 | `welcome_greeting_model.dart @0x35c76a4` |
| `ai_guide_shown` | `bool?` | yes | 3.24.3 | `welcome_greeting_model.dart @0x35c7704` |
| `calc_at` | `int?` | yes | 3.24.3 | `welcome_greeting_model.dart @0x35c777c` |
| `cleaned_proactive_message_count` | `int?` | yes | 3.24.3 | `welcome_greeting_model.dart @0x35c7810` |

### ProactiveCtaResponse

Answer of `proactive_cta`: suggested questions for a proactive scene.

`fromJson` `proactive_cta_response_model.dart @0x2e54954`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `questions` | `List?` of `ProactiveCtaItem` | yes | 3.24.3 | `proactive_cta_response_model.dart @0x2e5497c` |

### ProactiveCtaItem

One suggested question (title and value).

`fromJson` `proactive_cta_response_model.dart @0x2e54adc`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `title` | `String?` | yes | 3.24.3 | `proactive_cta_response_model.dart @0x2e54b08` |
| `value` | `String?` | yes | 3.24.3 | `proactive_cta_response_model.dart @0x2e54b7c` |

### QuestionBankResponse

Answer of `welcome_cta` and of the question-bank call (`get_question_bank`): a list of questions.

`fromJson` `question_bank_response_model.dart @0x2e56148`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `questions` | `List?` | yes | 3.24.3 | `question_bank_response_model.dart @0x2e56170` |

## Produced by

- [`get_all_config`](../api/smart_service/app/anka/get_all_config.md): `AnkaAgentEntryConfigModel` (`AnkaAgentEntryConfigModel.fromJson` call `anka_agent/http/anka_agent_http.dart @0x2737280`)
- [`get_menu_config`](../api/smart_service/app/anka/get_menu_config.md): `AnkaAgentMenuConfigModel` (`@0x35c5428`)
- [`setting`](../api/smart_service/app/anka/setting.md): `GetSettingResponse` (`@0x364e5ec`)
- [`welcome`](../api/smart_service/app/anka/welcome.md): `WelcomeGreetingModel` (`@0x35c7318`)
- [`proactive_cta`](../api/smart_service/app/anka/proactive_cta.md): `ProactiveCtaResponse` (`@0x2e54874`)
- [`welcome_cta`](../api/smart_service/app/anka/welcome_cta.md) and [`get_question_bank`](../api/smart_service/app/anka/get_question_bank.md): `QuestionBankResponse` (`@0x2e56068`, `@0x35c62b0`)

## Consumed by

The Anka agent pages and the AI EMS entry button (`ak_soft_ems/aiems/public_widget/anka_entry_button.dart`); field-level use is not traced.

## Changed since 3.18.0

Keys marked `3.24.3` in the tables are new in this app version (proactive messages, memory switch, bill analysis, power-outage switch, bubble configuration, setting and welcome models); the other keys are present in 3.18.0.

## Known unknowns

- Whether the switches (`*_switch`) are 0/1 integers on the wire (they are `int?` in the models) is inferred from the Dart types only.
- `setting_images` and the `list`-typed fields of the menu classes are `List` for the extractor; the element classes `SettingImageModel`, `MenuItem` and `SubItem` are read from the type arguments where present.
- `BubbleConfig.bubble_type` values are not decoded here.
