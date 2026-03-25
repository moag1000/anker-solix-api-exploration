# Passport

> 25 function calls, 24 unique endpoints

## `/passport/change_password`

- **changePwdRequest**(`account`) → `Result`

## `/passport/discount_desc`

- **getDisCountDesc**(`site_id, start_time, end_time, type`)

## `/passport/forget_password`

- **sendForgetPwdEmailRequest**(`client_id, redirect_uri, response_type, scope, state`)

## `/passport/freeze_account`

- **freezeAccount**(`password, verify_kind, export_account, client_secret_info, public_key`)

## `/passport/get_profile`

- **getUserProfileRequest**(`*(no params extracted)*`) → `UserModel`

## `/passport/get_subscriptions`

- **getSubscription**(`*(no params extracted)*`) → `SubscribeEmailModel`

## `/passport/get_user_param`

- **getAppSwitchApi**(`user_params, param_type, param_value`) → `UserParamModel`

## `/passport/login`

- **iotLoginRequest**(`phone_number, verify_code, client_secret_info, public_key`) → `IotUserModel`

## `/passport/logout`

- **logOutRequest**(`*(no params extracted)*`) → `Result`

## `/passport/phone_bind_account`

- **bindPhoneNumberRequest**(`phone_number, kind`) → `IotUserModel`

## `/passport/phone_code_list`

- **getPreDirectionPhoneCode**(`device_sn, type, device_sns`)

## `/passport/phone_reset_password`

- **sendForgetPwdPhoneRequest**(`email`)

## `/passport/phone_verification_code`

- **sendVerifyCodeRequest**(`email`)

## `/passport/phone_verification_login`

- **verifyCodeLoginRequest**(`email, password, is_subscribe, country_code`) → `IotUserModel`

## `/passport/phone_verification_regist`

- **verifyCodeRegisterRequest**(`*(no params extracted)*`) → `UserModel`

## `/passport/register`

- **registerRequest**(`phone_number, verify_code, password, client_secret_info, public_key, is_subscribe, country_code`) → `UserModel`

## `/passport/resend_active_email`

- **sendVerifyEmailRequest**(`file_name, content_type, file_size, disable_ssl, type`) → `Result`

## `/passport/set_account_password`

- **userSetPasswordApi**(`*(no params extracted)*`)

## `/passport/set_subscriptions`

- **setSubscription**(`email`)

## `/passport/subscription_configs`

- **getSubscriptionConfigs**(`*(no params extracted)*`)

## `/passport/third_party_login`

- **thirdLoginRequest**(`email, password, client_secret_info, public_key`) → `IotUserModel`

## `/passport/update_profile`

- **updateUserProfileRequest**(`password, original_password`) → `UserModel`

## `/passport/update_user_param`

- **setAppSwitchApi**(`*(no params extracted)*`)

## `/passport/validate_email`

- **validateAccountRequest**(`site_id, status`) → `ValidateAccountModel`
- **checkIsRegisterRequest**(`phone_number, verify_code, password, client_secret_info, public_key`) → `ValidateAccountModel`

