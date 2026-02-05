# WebSocket / Market Channel（市场频道）

> 页面：/developers/CLOB/websocket/market-channel  
> 说明：该频道为 **Public channel**，用于市场更新（Level 2 价格数据）。页面原文写法：`SUBSCRIBE <wss-channel> market`。  [oai_citation:0‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel)

---

## 1) 接口名称：Market Channel 订阅（SUBSCRIBE）

| 项 | 值 |
|---|---|
| 请求方法 | SUBSCRIBE（WebSocket 订阅指令）  [oai_citation:1‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| Endpoint（完整路径） | `<wss-channel> market`（页面原文如此标注）  [oai_citation:2‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 请求参数

> 本页面仅给出了订阅指令文本：`SUBSCRIBE <wss-channel> market`，未给出 JSON 请求体字段定义。

| 字段名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| `<wss-channel>` | string（占位符） | 是 | 页面中用作占位，代表 WebSocket channel/endpoint 的前缀  [oai_citation:3‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `market` | string（固定字面量） | 是 | 订阅 market channel（固定写为 `market`）  [oai_citation:4‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 返回参数

> 订阅成功后，服务端会推送下述多种消息（message）。本节不单独定义返回字段，见各消息结构。

---

## 2) 接口名称：book Message（订单簿快照/更新）

| 项 | 值 |
|---|---|
| 请求方法 | WebSocket（服务端推送）  [oai_citation:5‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| Endpoint（完整路径） | `<wss-channel> market`  [oai_citation:6‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| （无） | — | — | 本消息为服务端推送  [oai_citation:7‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 返回参数（Structure）

| 字段名 | 类型 | 说明 |
|---|---|---|
| `event_type` | string | `"book"`  [oai_citation:8‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `asset_id` | string | asset ID（token ID）  [oai_citation:9‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `market` | string | condition ID of market  [oai_citation:10‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `timestamp` | string | unix timestamp：当前 book 生成时间（毫秒，1/1,000 秒）  [oai_citation:11‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `hash` | string | hash summary of the orderbook content  [oai_citation:12‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `buys` | `OrderSummary[]` | aggregate book levels for buys（元素类型为 size/price）  [oai_citation:13‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `sells` | `OrderSummary[]` | aggregate book levels for sells（元素类型为 size/price）  [oai_citation:14‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

#### — OrderSummary（对象结构）

| 字段名 | 类型 | 说明 |
|---|---|---|
| `price` | string | size available at that price level（页面原文描述如此）  [oai_citation:15‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `size` | string | price of the orderbook level（页面原文描述如此）  [oai_citation:16‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

> ⚠️ 注意：同一页面的示例响应字段使用了 `bids`/`asks`，而结构表写的是 `buys`/`sells`。两者均为页面可见内容：  
> - 结构表：`buys`/`sells`  [oai_citation:17‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel)  
> - 示例：`bids`/`asks`  [oai_citation:18‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel)  

---

## 3) 接口名称：price_change Message（价格档位变更）

| 项 | 值 |
|---|---|
| 请求方法 | WebSocket（服务端推送）  [oai_citation:19‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| Endpoint（完整路径） | `<wss-channel> market`  [oai_citation:20‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| （无） | — | — | 本消息为服务端推送  [oai_citation:21‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 返回参数（Structure）

| 字段名 | 类型 | 说明 |
|---|---|---|
| `event_type` | string | `"price_change"`  [oai_citation:22‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `market` | string | condition ID of market  [oai_citation:23‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `price_changes` | `PriceChange[]` | array of price change objects  [oai_citation:24‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `timestamp` | string | unix timestamp in milliseconds  [oai_citation:25‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

#### — PriceChange（对象结构）

| 字段名 | 类型 | 说明 |
|---|---|---|
| `asset_id` | string | asset ID（token ID）  [oai_citation:26‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `price` | string | price level affected  [oai_citation:27‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `size` | string | new aggregate size for price level  [oai_citation:28‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `side` | string | `"BUY"` or `"SELL"`  [oai_citation:29‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `hash` | string | hash of the order  [oai_citation:30‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `best_bid` | string | current best bid price  [oai_citation:31‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `best_ask` | string | current best ask price  [oai_citation:32‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

> ⚠️ Breaking Change Notice（页面原文）：`price_change` schema 将在 **September 15, 2025 at 11 PM UTC** 更新，并给出 migration guide 链接。  [oai_citation:33‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel)

---

## 4) 接口名称：tick_size_change Message（最小 tick 变化）

| 项 | 值 |
|---|---|
| 请求方法 | WebSocket（服务端推送）  [oai_citation:34‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| Endpoint（完整路径） | `<wss-channel> market`  [oai_citation:35‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| （无） | — | — | 本消息为服务端推送  [oai_citation:36‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 返回参数（Structure）

| 字段名 | 类型 | 说明 |
|---|---|---|
| `event_type` | string | **页面结构表写为** `"price_change"`（原文如此）  [oai_citation:37‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `asset_id` | string | asset ID（token ID）  [oai_citation:38‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `market` | string | condition ID of market  [oai_citation:39‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `old_tick_size` | string | previous minimum tick size  [oai_citation:40‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `new_tick_size` | string | current minimum tick size  [oai_citation:41‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `side` | string | buy/sell  [oai_citation:42‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `timestamp` | string | time of event  [oai_citation:43‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

> ⚠️ 注意：同页示例响应中 `event_type` 为 `"tick_size_change"`，与结构表 `event_type: "price_change"` 不一致；两者均为页面可见内容。  [oai_citation:44‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel)

---

## 5) 接口名称：last_trade_price Message（最新成交价）

| 项 | 值 |
|---|---|
| 请求方法 | WebSocket（服务端推送）  [oai_citation:45‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| Endpoint（完整路径） | `<wss-channel> market`  [oai_citation:46‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| （无） | — | — | 本消息为服务端推送  [oai_citation:47‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 返回参数（Response 示例可见字段）

> 本页未给出 “Structure” 表，仅给出示例响应，因此以下字段以示例为准。

| 字段名 | 类型 | 说明 |
|---|---|---|
| `asset_id` | string | asset id（示例字段）  [oai_citation:48‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `event_type` | string | `"last_trade_price"`  [oai_citation:49‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `fee_rate_bps` | string | fee rate in bps（示例字段名）  [oai_citation:50‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `market` | string | market（condition ID）  [oai_citation:51‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `price` | string | price（示例字段）  [oai_citation:52‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `side` | string | side（示例为 `"BUY"`）  [oai_citation:53‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `size` | string | size（示例字段）  [oai_citation:54‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `timestamp` | string | unix timestamp in milliseconds（示例值为毫秒时间戳字符串）  [oai_citation:55‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

---

## 6) 接口名称：best_bid_ask Message（最优买卖价）

| 项 | 值 |
|---|---|
| 请求方法 | WebSocket（服务端推送）  [oai_citation:56‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| Endpoint（完整路径） | `<wss-channel> market`  [oai_citation:57‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| （无） | — | — | 本消息为服务端推送  [oai_citation:58‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 返回参数（Structure）

| 字段名 | 类型 | 说明 |
|---|---|---|
| `event_type` | string | `"best_bid_ask"`  [oai_citation:59‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `market` | string | condition ID of market  [oai_citation:60‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `asset_id` | string | asset ID（token ID）  [oai_citation:61‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `best_bid` | string | current best bid price  [oai_citation:62‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `best_ask` | string | current best ask price  [oai_citation:63‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `spread` | string | spread between best bid and ask  [oai_citation:64‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `timestamp` | string | unix timestamp in milliseconds  [oai_citation:65‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

> 备注（页面原文）：该消息在 `custom_feature_enabled` flag 之后可用。  [oai_citation:66‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel)

---

## 7) 接口名称：new_market Message（新市场创建）

| 项 | 值 |
|---|---|
| 请求方法 | WebSocket（服务端推送）  [oai_citation:67‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| Endpoint（完整路径） | `<wss-channel> market`  [oai_citation:68‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| （无） | — | — | 本消息为服务端推送  [oai_citation:69‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 返回参数（Structure）

| 字段名 | 类型 | 说明 |
|---|---|---|
| `id` | string | market ID  [oai_citation:70‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `question` | string | market question  [oai_citation:71‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `market` | string | condition ID of market  [oai_citation:72‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `slug` | string | market slug  [oai_citation:73‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `description` | string | market description  [oai_citation:74‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `assets_ids` | string[] | list of asset IDs  [oai_citation:75‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `outcomes` | string[] | list of outcomes  [oai_citation:76‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `event_message` | object | event message object  [oai_citation:77‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `timestamp` | string | unix timestamp in milliseconds  [oai_citation:78‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `event_type` | string | `"new_market"`  [oai_citation:79‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

#### — EventMessage（对象结构）

| 字段名 | 类型 | 说明 |
|---|---|---|
| `id` | string | event message ID  [oai_citation:80‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `ticker` | string | event message ticker  [oai_citation:81‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `slug` | string | event message slug  [oai_citation:82‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `title` | string | event message title  [oai_citation:83‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `description` | string | event message description  [oai_citation:84‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

> 备注（页面原文）：该消息在 `custom_feature_enabled` flag 之后可用。  [oai_citation:85‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel)

---

## 8) 接口名称：market_resolved Message（市场已结算/已解析）

| 项 | 值 |
|---|---|
| 请求方法 | WebSocket（服务端推送）  [oai_citation:86‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| Endpoint（完整路径） | `<wss-channel> market`  [oai_citation:87‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 请求参数

| 字段名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| （无） | — | — | 本消息为服务端推送  [oai_citation:88‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

### 返回参数（Structure）

| 字段名 | 类型 | 说明 |
|---|---|---|
| `id` | string | market ID  [oai_citation:89‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `question` | string | market question  [oai_citation:90‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `market` | string | condition ID of market  [oai_citation:91‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `slug` | string | market slug  [oai_citation:92‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `description` | string | market description  [oai_citation:93‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `assets_ids` | string[] | list of asset IDs  [oai_citation:94‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `outcomes` | string[] | list of outcomes  [oai_citation:95‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `winning_asset_id` | string | winning asset ID  [oai_citation:96‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `winning_outcome` | string | winning outcome  [oai_citation:97‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `event_message` | object | event message object  [oai_citation:98‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `timestamp` | string | unix timestamp in milliseconds  [oai_citation:99‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `event_type` | string | `"market_resolved"`  [oai_citation:100‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

#### — EventMessage（对象结构）

| 字段名 | 类型 | 说明 |
|---|---|---|
| `id` | string | event message ID  [oai_citation:101‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `ticker` | string | event message ticker  [oai_citation:102‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `slug` | string | event message slug  [oai_citation:103‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `title` | string | event message title  [oai_citation:104‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |
| `description` | string | event message description  [oai_citation:105‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel) |

> ⚠️ 注意：同页示例响应末尾的 `event_type` 字段值显示为 `"new_market"`（而结构表写为 `"market_resolved"`）；两者均为页面可见内容。  [oai_citation:106‡Polymarket 文档](https://docs.polymarket.com/developers/CLOB/websocket/market-channel)