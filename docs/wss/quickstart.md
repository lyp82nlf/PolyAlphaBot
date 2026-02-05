# Polymarket Websocket — WSS Quickstart（基于单页：/quickstart/websocket/WSS-Quickstart）

> 说明：本页主要通过代码示例展示如何连接 **Market** 与 **User** 两类 WebSocket 通道，以及如何发送订阅/退订消息；**未在本页给出服务器推送消息的详细字段结构**（只展示了 `on_message` 收到的原始 `message`）。

---

## 1) 连接 Market WebSocket（握手）

- **接口名称**：Connect Market WebSocket
- **请求方法**：GET（WebSocket Upgrade 握手）
- **Endpoint（完整路径）**：`wss://ws-subscriptions-clob.polymarket.com/ws/market`
- **请求参数**：

| 字段名 | 类型 | 必填 | 说明 |
|---|---:|:---:|---|
| （无） | - | - | 本页示例中 URL 仅包含 path：`/ws/market` |

- **返回参数**：

| 字段名 | 类型 | 说明 |
|---|---:|---|
| message | string | 本页示例仅展示回调 `on_message(self, ws, message)` 收到的原始文本消息（未定义 JSON 字段结构） |

---

## 2) Market 通道初始化订阅消息（连接成功后首次发送）

- **接口名称**：Market Init Subscribe
- **请求方法**：WS SEND（WebSocket 文本帧，JSON）
- **Endpoint（完整路径）**：`wss://ws-subscriptions-clob.polymarket.com/ws/market`
- **请求参数**（发送 JSON）：

| 字段名 | 类型 | 必填 | 说明 |
|---|---:|:---:|---|
| type | string | 是 | 固定为 `"market"` |
| assets_ids | array[string] | 是 | 要订阅的资产/Token ID 列表（示例为超长数字字符串） |

- **返回参数**：

| 字段名 | 类型 | 说明 |
|---|---:|---|
| message | string | 本页未提供返回 JSON 字段；仅说明会在 `on_message` 收到原始消息 |

---

## 3) Market 通道动态订阅（subscribe）

- **接口名称**：Market Subscribe
- **请求方法**：WS SEND（WebSocket 文本帧，JSON）
- **Endpoint（完整路径）**：`wss://ws-subscriptions-clob.polymarket.com/ws/market`
- **请求参数**（发送 JSON）：

| 字段名 | 类型 | 必填 | 说明 |
|---|---:|:---:|---|
| operation | string | 是 | 固定为 `"subscribe"` |
| assets_ids | array[string] | 是 | 要新增订阅的资产/Token ID 列表 |

- **返回参数**：

| 字段名 | 类型 | 说明 |
|---|---:|---|
| message | string | 本页未提供返回 JSON 字段；仅说明会在 `on_message` 收到原始消息 |

---

## 4) Market 通道动态退订（unsubscribe）

- **接口名称**：Market Unsubscribe
- **请求方法**：WS SEND（WebSocket 文本帧，JSON）
- **Endpoint（完整路径）**：`wss://ws-subscriptions-clob.polymarket.com/ws/market`
- **请求参数**（发送 JSON）：

| 字段名 | 类型 | 必填 | 说明 |
|---|---:|:---:|---|
| operation | string | 是 | 固定为 `"unsubscribe"` |
| assets_ids | array[string] | 是 | 要取消订阅的资产/Token ID 列表 |

- **返回参数**：

| 字段名 | 类型 | 说明 |
|---|---:|---|
| message | string | 本页未提供返回 JSON 字段；仅说明会在 `on_message` 收到原始消息 |

---

## 5) 连接 User WebSocket（握手）

- **接口名称**：Connect User WebSocket
- **请求方法**：GET（WebSocket Upgrade 握手）
- **Endpoint（完整路径）**：`wss://ws-subscriptions-clob.polymarket.com/ws/user`
- **请求参数**：

| 字段名 | 类型 | 必填 | 说明 |
|---|---:|:---:|---|
| （无） | - | - | 本页示例中 URL 仅包含 path：`/ws/user` |

- **返回参数**：

| 字段名 | 类型 | 说明 |
|---|---:|---|
| message | string | 本页示例仅展示 `on_message` 收到的原始文本消息（未定义 JSON 字段结构） |

---

## 6) User 通道初始化订阅消息（连接成功后首次发送，带鉴权）

- **接口名称**：User Init Subscribe (with Auth)
- **请求方法**：WS SEND（WebSocket 文本帧，JSON）
- **Endpoint（完整路径）**：`wss://ws-subscriptions-clob.polymarket.com/ws/user`
- **请求参数**（发送 JSON）：

| 字段名 | 类型 | 必填 | 说明 |
|---|---:|:---:|---|
| type | string | 是 | 固定为 `"user"` |
| markets | array[string] | 是 | 示例里传入的是 `condition_ids`（本页注释：`# no really need to filter by this one`） |
| auth | object | 是 | 鉴权信息对象 |
| — apiKey | string | 是 | API Key（从已初始化 client 导出） |
| — secret | string | 是 | API Secret（从已初始化 client 导出） |
| — passphrase | string | 是 | API Passphrase（从已初始化 client 导出） |

- **返回参数**：

| 字段名 | 类型 | 说明 |
|---|---:|---|
| message | string | 本页未提供返回 JSON 字段；仅说明会在 `on_message` 收到原始消息 |

---

## 7) Ping（保活）

- **接口名称**：Ping Keepalive
- **请求方法**：WS SEND（WebSocket 文本帧，纯文本）
- **Endpoint（完整路径）**：`wss://ws-subscriptions-clob.polymarket.com/ws/{market|user}`
- **请求参数**：

| 字段名 | 类型 | 必填 | 说明 |
|---|---:|:---:|---|
| （payload） | string | 是 | 固定发送 `"PING"`（示例每 10 秒一次） |

- **返回参数**：

| 字段名 | 类型 | 说明 |
|---|---:|---|
| message | string | 本页未定义 PING 的响应结构；仅展示 `on_message` 会收到消息 |

---

## 8)（本页出现但非 HTTP API）Derive API Keys（通过示例 SDK 调用）

- **接口名称**：Derive API Keys（SDK 调用）
- **请求方法**：N/A（本页未给出对应 HTTP 请求方法/路径）
- **Endpoint（完整路径）**：Host 示例：`https://clob.polymarket.com`（仅展示 host）
- **请求参数**（示例变量）：

| 字段名 | 类型 | 必填 | 说明 |
|---|---:|:---:|---|
| host | string | 是 | 固定示例：`https://clob.polymarket.com` |
| key | string | 是 | Private Key（示例注释：email login 可从指定页面导出；或来自 Web3 应用） |
| chain_id | int | 是 | 示例固定：`137`（注释：无需调整） |
| signature_type | int | 否 | 示例给出两种：`1`（Email/Magic 代理钱包）、`2`（浏览器钱包代理钱包）；EOA 直连示例不传 |
| funder | string | 否 | `POLYMARKET_PROXY_ADDRESS`：你入金/发送 USDC 的代理地址（使用代理钱包时传） |

- **返回参数**：

| 字段名 | 类型 | 说明 |
|---|---:|---|
| （整体返回值） | unknown | 本页仅 `print(client.derive_api_key())`，未列出返回字段结构（因此无法在本页内 100% 还原字段） |