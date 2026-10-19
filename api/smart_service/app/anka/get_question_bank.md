> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_question_bank

## Purpose

Reads the recommended questions of the Anka assistant for the AI EMS source (the chat controller fetches them in `_fetchAiEmsRecommendQuestions`). The URL literal has a double slash after `v1`.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /smart_service/v1//app/anka/get_question_bank` (asm-traced). Sender: `AnkaAgentHttp.getQuestionBank` (`anka_agent/http/anka_agent_http.dart @0x35c60f8`); the URL literal is loaded at `@0x35c61cc` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x35c61c4`).

## Encrypted?

Yes by wrapper (asm-traced): `getQuestionBank` calls `HttpServiceImpl.encryptionRequestHttpByGHttpRequest` (`anka_agent/http/anka_agent_http.dart @0x35c61f4`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). The wrapper sends through the global `HttpRequest` object (`gHttpRequest`). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

Body is a `<String, String>` map of one pair (`r2 = 4`, `@0x35c613c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `source` | String | yes (constant) | `"aiems"` | `anka_agent_http.dart @0x35c6144`; value `"aiems"` `@0x35c614c` |

## `param_type`/`cmd`

n/a

## Response model (link)

`QuestionBankResponse` ([../../../../models/anka_agent_models.md](../../../../models/anka_agent_models.md#questionbankresponse)): `QuestionBankResponse.fromJson` is called in the success closure (`anka_agent_http.dart @0x35c62b0`).

## Response

The success closure parses the data into the model.

| field | type | required | example | source |
|---|---|---|---|---|
| `questions` | list | no |  | `question_bank_response_model.dart @0x2e56170`; [model page](../../../../models/anka_agent_models.md#questionbankresponse) |

## Example request/response

Request, synthesized

```json
{ "source": "aiems" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `AiChatController._fetchAiEmsRecommendQuestions` (`anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c60dc`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0xf07e8`). since: 3.24.3.

## Known unknowns

- The URL is `/smart_service/v1//app/anka/get_question_bank` (two slashes, `pp+0xf07e8`); whether the server normalises the path or the double slash is part of the real route is not known.
- This URL is not in `data/endpoints.json`: the inventory extractor did not pick the literal up (reported as a tool finding), so this page is hand-added.

## Device-tested by

none
