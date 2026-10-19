> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# welcome_cta

## Purpose

Reads the suggested questions (call-to-action chips) that go with the welcome greeting of the Anka assistant.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /smart_service/v1/app/anka/welcome_cta` (asm-traced). Sender: `AnkaAgentHttp.getWelcomeCta` (`anka_agent/http/anka_agent_http.dart @0x2e55c54`); the URL literal is loaded at `@0x2e55e0c` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x2e55e04`).

## Encrypted?

Yes by wrapper (asm-traced): `getWelcomeCta` calls `HttpServiceImpl.encryptionRequestHttpByGHttpRequest` (`anka_agent/http/anka_agent_http.dart @0x2e55e34`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). The wrapper sends through the global `HttpRequest` object (`gHttpRequest`). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

Body is a `<String, dynamic>` map of three pairs (`r2 = 12`, `@0x2e55ca4`).

| field | type | required | example | source |
|---|---|---|---|---|
| `current_time` | String | yes | `"2026-10-19 14:30:00"` | `anka_agent_http.dart @0x2e55cb0`; first argument |
| `welcome_type` | String | yes | `<welcome type>` | `anka_agent_http.dart @0x2e55cc4`; value from the greeting (the `welcome_type` of the `welcome` answer is the likely source, not traced) |
| `site_count` | int | yes | `1` | `anka_agent_http.dart @0x2e55cd8`; boxed with `BoxInt64Instr` (`@0x2e55ce8`), unboxed int64 |

## `param_type`/`cmd`

n/a

## Response model (link)

`QuestionBankResponse` ([../../../../models/anka_agent_models.md](../../../../models/anka_agent_models.md#questionbankresponse)): `QuestionBankResponse.fromJson` is called in the success closure (`anka_agent_http.dart @0x2e56068`).

## Response

The success closure parses the data into the model.

| field | type | required | example | source |
|---|---|---|---|---|
| `questions` | list | no |  | `question_bank_response_model.dart @0x2e56170`; [model page](../../../../models/anka_agent_models.md#questionbankresponse) |

## Example request/response

Request, synthesized

```json
{ "current_time": "<time>", "welcome_type": "<welcome type>", "site_count": 1 }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `AiChatController.refreshWelcomeCta` (`anka_agent/pages/home/controller/ai_chat_controller.dart @0x2e55c18`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0xefde8`). since: 3.24.3.

## Known unknowns

- The element type of `questions` is not read here (the proactive call uses `ProactiveCtaItem` with `title` and `value`).

## Device-tested by

none
