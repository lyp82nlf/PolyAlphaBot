## Get current positions for a user

- 接口名称：Get current positions for a user
- 请求方法：GET
- Endpoint（完整路径）：https://data-api.polymarket.com/positions

### 请求参数（Query Parameters）

| 字段名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| user | string | 是 | User address (required) User Profile Address (0x-prefixed, 40 hex chars) |
| market | string[] | 否 | Comma-separated list of condition IDs. Mutually exclusive with eventId. 0x-prefixed 64-hex string |
| eventId | integer[] | 否 | Comma-separated list of event IDs. Mutually exclusive with market. Required range: `x >= 1` |
| sizeThreshold | number | 否 | default: `1`。Required range: `x >= 0` |
| redeemable | boolean | 否 | default: `false` |
| mergeable | boolean | 否 | default: `false` |
| limit | integer | 否 | default: `100`。Required range: `0 <= x <= 500` |
| offset | integer | 否 | default: `0`。Required range: `0 <= x <= 10000` |
| sortBy | enum<string> | 否 | default: `TOKENS`。Available options: `CURRENT`, `INITIAL`, `TOKENS`, `CASHPNL`, `PERCENTPNL`, `TITLE`, `RESOLVING`, `PRICE`, `AVGPRICE` |
| sortDirection | enum<string> | 否 | default: `DESC`。Available options: `ASC`, `DESC` |
| title | string | 否 | Maximum string length: `100` |

### 返回参数（Response 200: application/json）

> 返回类型：array<object>

| 字段名 | 类型 | 说明 |
|---|---|---|
| [] | array<object> | Success |
| — proxyWallet | string | User Profile Address (0x-prefixed, 40 hex chars) |
| — asset | string |  |
| — conditionId | string | 0x-prefixed 64-hex string |
| — size | number |  |
| — avgPrice | number |  |
| — initialValue | number |  |
| — currentValue | number |  |
| — cashPnl | number |  |
| — percentPnl | number |  |
| — totalBought | number |  |
| — realizedPnl | number |  |
| — percentRealizedPnl | number |  |
| — curPrice | number |  |
| — redeemable | boolean |  |
| — mergeable | boolean |  |
| — title | string |  |
| — slug | string |  |
| — icon | string |  |
| — eventSlug | string |  |
| — outcome | string |  |
| — outcomeIndex | integer |  |
| — oppositeOutcome | string |  |
| — oppositeAsset | string |  |
| — endDate | string |  |
| — negativeRisk | boolean |  |