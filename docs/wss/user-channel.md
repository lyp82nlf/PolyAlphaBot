# User Channel（Websocket）

> 页面说明：Authenticated channel for updates related to user activities (orders, trades), filtered for authenticated user by apikey.  
> 订阅方式：SUBSCRIBE `<wss-channel> user`

---

## 1) 接口名称：Trade Message（交易消息）

### 请求方法
WebSocket（Server Push / 事件推送）

### Endpoint（完整路径）
`<wss-channel> user`

### 请求参数
无（该页面未提供该消息的“客户端请求字段/订阅请求结构”，仅描述服务端推送的消息结构）

### 返回参数（Trade Message Payload）
| 字段名 | 类型 | 说明 |
|---|---|---|
| asset_id | string | asset id (token ID) of order (market order) |
| event_type | string | “trade” |
| id | string | trade id |
| last_update | string | time of last update to trade |
| maker_orders | MakerOrder[] | array of maker order details |
| market | string | market identifier (condition ID) |
| matchtime | string | time trade was matched |
| outcome | string | outcome |
| owner | string | api key of event owner |
| price | string | price |
| side | string | BUY/SELL |
| size | string | size |
| status | string | trade status |
| taker_order_id | string | id of taker order |
| timestamp | string | time of event |
| trade_owner | string | api key of trade owner |
| type | string | “TRADE” |

#### — maker_orders（MakerOrder 对象结构）
| 字段名 | 类型 | 说明 |
|---|---|---|
| — asset_id | string | asset of the maker order |
| — matched_amount | string | amount of maker order matched in trade |
| — order_id | string | maker order ID |
| — outcome | string | outcome |
| — owner | string | owner of maker order |
| — price | string | price of maker order |

---

## 2) 接口名称：Order Message（订单消息）

### 请求方法
WebSocket（Server Push / 事件推送）

### Endpoint（完整路径）
`<wss-channel> user`

### 请求参数
无（该页面未提供该消息的“客户端请求字段/订阅请求结构”，仅描述服务端推送的消息结构）

### 返回参数（Order Message Payload）
| 字段名 | 类型 | 说明 |
|---|---|---|
| asset_id | string | asset ID (token ID) of order |
| associate_trades | string[] | array of ids referencing trades that the order has been included in |
| event_type | string | “order” |
| id | string | order id |
| market | string | condition ID of market |
| order_owner | string | owner of order |
| original_size | string | original order size |
| outcome | string | outcome |
| owner | string | owner of orders |
| price | string | price of order |
| side | string | BUY/SELL |
| size_matched | string | size of order that has been matched |
| timestamp | string | time of event |
| type | string | PLACEMENT/UPDATE/CANCELLATION |