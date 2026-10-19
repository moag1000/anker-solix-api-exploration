> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Flows

This directory holds step traces of user-visible actions (`<name>.md`), each a sequence of links to the endpoint, param_type, MQTT or BLE owner pages that carry the facts. Flow pages contain no payload copies.

Pages on disk:

- [system_output_limit.md](system_output_limit.md) — system output limit
- [encrypted_request.md](encrypted_request.md) — encrypted request
- [modbus_setup.md](modbus_setup.md) — Modbus setup (third-party control)

The old [../FLOWS.md](../FLOWS.md) is a 3.18.0 reference with known Smi errors (see the Errata in [../CHANGELOG.md](../CHANGELOG.md)); its remaining flows are not yet rebuilt here.

Not here: payload, field or opcode definitions; those live with their owners, see [../docs/STRUCTURE.md](../docs/STRUCTURE.md).
