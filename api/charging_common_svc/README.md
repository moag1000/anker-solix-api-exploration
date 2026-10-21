> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# charging_common_svc

Service index for the URL prefix `/charging_common_svc/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/charging_common_svc/location/get`](location/get.md) | Reads the saved or default weather/price location of a site (callers `ElectricityPlaceSmartLogic::onReady`, `LocalAutoDisasterFeature::refreshLocation`, `YesterdayEarningTipsLogic::_fetchLocation`, `WeatherManager::fetchDefaultLocation`, `ChargingWeatherHttpAdapter::fetchSavedLocation`; UI callers `ElectricityPlaceSmartView::_refreshAutoDisasterLocation`, `PlaceSelectionHelper::_loadInitialPlace`, `WeatherService::_fetchWeatherData`) (string-only: the caller names are in the page's caller list, the chain is not in `data/endpoints.json`). | - | owner |
| [`/charging_common_svc/location/set`](location/set.md) | Saves the location a user picked for a site (callers `LocalAutoDisasterFeature::_setLocation`, reached from `LocalAutoDisasterFeature::pushToMap`, and `ChargingWeatherHttpAdapter::saveLocation`, reached from `WeatherService::syncLocation`) (string-only: the caller names come from the page's caller list, the chain is not in `data/endpoints.json`). | - | owner |
| [`/charging_common_svc/location/support`](location/support.md) | Asks which locations (country codes) the AI-mode / dynamic-price features support for a site (callers `EmsAiModeConditionLogic::getSupportLocation` and `HttpRequestControllerImpl::getLocationSupport`; UI callers `EmsAiModeConditionLogic::onReady`, `AiModeConditionLogic::getSupportLocation`, `StationHomeSettingsLogic::getSupportLocation`) (string-only: inferred from the caller names, the chain is not in `data/endpoints.json`). | - | owner |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
