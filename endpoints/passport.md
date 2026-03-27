# Passport

> 25 function calls, 24 unique endpoints
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)
>
> **HA relevance**: Only `login` and `token refresh` are relevant for HA integration.
> All other endpoints (account management, email verification, third-party auth,
> GDPR) are **not relevant** — they handle app account lifecycle, not device control.
> Note: Passport endpoints are not covered in ENDPOINT_FIELDS.md (which focuses on power/charging/app endpoints). These endpoints were discovered in the Blutter decompilation but their parameters were not extractable from the same code paths. Parameters shown as `*(no params in ENDPOINT_FIELDS.md)*` need verification via API testing.

## `/passport/change_password`

- **changePwdRequest**(`*(no params in ENDPOINT_FIELDS.md)*`) → `Result`

## `/passport/discount_desc`

- **getDisCountDesc**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/passport/forget_password`

- **sendForgetPwdEmailRequest**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/passport/freeze_account`

- **freezeAccount**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/passport/get_profile`

- **getUserProfileRequest**(`*(none extracted)*`) → `UserModel`

## `/passport/get_subscriptions`

- **getSubscription**(`*(none extracted)*`) → `SubscribeEmailModel`

## `/passport/get_user_param`

- **getAppSwitchApi**(`*(no params in ENDPOINT_FIELDS.md)*`) → `UserParamModel`

## `/passport/login`

- **iotLoginRequest**(`*(no params in ENDPOINT_FIELDS.md)*`) → `IotUserModel`

## `/passport/logout`

- **logOutRequest**(`*(none extracted)*`) → `Result`

## `/passport/phone_bind_account`

- **bindPhoneNumberRequest**(`*(no params in ENDPOINT_FIELDS.md)*`) → `IotUserModel`

## `/passport/phone_code_list`

- **getPreDirectionPhoneCode**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/passport/phone_reset_password`

- **sendForgetPwdPhoneRequest**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/passport/phone_verification_code`

- **sendVerifyCodeRequest**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/passport/phone_verification_login`

- **verifyCodeLoginRequest**(`*(no params in ENDPOINT_FIELDS.md)*`) → `IotUserModel`

## `/passport/phone_verification_regist`

- **verifyCodeRegisterRequest**(`*(none extracted)*`) → `UserModel`

## `/passport/register`

- **registerRequest**(`*(no params in ENDPOINT_FIELDS.md)*`) → `UserModel`

## `/passport/resend_active_email`

- **sendVerifyEmailRequest**(`*(no params in ENDPOINT_FIELDS.md)*`) → `Result`

## `/passport/set_account_password`

- **userSetPasswordApi**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/passport/set_subscriptions`

- **setSubscription**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/passport/subscription_configs`

- **getSubscriptionConfigs**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/passport/third_party_login`

- **thirdLoginRequest**(`*(no params in ENDPOINT_FIELDS.md)*`) → `IotUserModel`

## `/passport/update_profile`

- **updateUserProfileRequest**(`*(no params in ENDPOINT_FIELDS.md)*`) → `UserModel`

## `/passport/update_user_param`

- **setAppSwitchApi**(`*(no params in ENDPOINT_FIELDS.md)*`)

## `/passport/validate_email`

- **validateAccountRequest**(`*(no params in ENDPOINT_FIELDS.md)*`) → `ValidateAccountModel`
- **checkIsRegisterRequest**(`*(no params in ENDPOINT_FIELDS.md)*`) → `ValidateAccountModel`
