# Charging Pv Svc

> 4 function calls, 4 unique endpoints
>
> **Source**: Regenerated from ENDPOINT_FIELDS.md (authoritative reference)

## `/charging_pv_svc/getPvStatus`

- **getPvStatus**(`sns?`) → `A5140DeviceStatus`

## `/charging_pv_svc/selectUserTieredElecPrice`

- **selectUserTieredElecPrice**(`sn?`) → `CurrencyElecModel`

## `/charging_pv_svc/updateUserTieredElecPrice`

- **updateUserTieredElecPrice**(`sn, currencyUnit, tieredElecPrices`)
  - Upstream-confirmed: `tieredElecPrices` = `[{"from": "00:00", "to": "23:59", "price": 0.30}]`

## `/charging_pv_svc/set_aps_power`

- **set_device_pv_power**(`sn, power`)
  - Upstream-confirmed: sets standalone inverter power limit in Watts
