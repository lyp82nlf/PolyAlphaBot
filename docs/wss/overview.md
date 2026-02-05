# WSS Overview（Polymarket CLOB Websocket）

> 说明：本页为 WebSocket 总览/订阅说明页，仅描述“订阅请求消息”的字段；**本页未提供 WebSocket URL（wss://...）与任何返回消息（push events）的字段结构**。

---

## 1) 初始订阅消息（连接建立后发送）

### 接口名称
WSS Subscription（Initial Subscribe Message）

### 请求方法
WebSocket（JSON Message）

### Endpoint（完整路径）
本页未提供 WebSocket URL / 路径（仅说明有 `user` 与 `market` 两个 channel）

### 请求参数

| 字段名 | 类型 | 是否必填 | 说明 |
|---|---|---|---|
| auth | Auth | 是 | 认证信息；本页仅声明其类型为 `Auth`，具体结构需见 “WSS Authentication” 页面 |
| markets | string[] | 否 | 需要接收事件的 markets（condition IDs）；用于 `user` channel |
| assets_ids | string[] | 否 | 需要接收事件的 asset ids（token IDs）；用于 `market` channel |
| type | string | 是 | 要订阅的 channel 标识（USER 或 MARKET） |
| custom_feature_enabled | bool | 否 | 启用 / 禁用自定义功能 |

### 返回参数
本页未提供任何“返回/推送消息（events）”的结构与字段列表

---

## 2) 运行中追加/取消订阅资产（Subscribe / Unsubscribe More Assets）

### 接口名称
WSS Subscribe / Unsubscribe to More Assets（Post-Connect）

### 请求方法
WebSocket（JSON Message）

### Endpoint（完整路径）
本页未提供 WebSocket URL / 路径（在已建立连接的同一 WebSocket 上发送消息）

### 请求参数

| 字段名 | 类型 | 是否必填 | 说明 |
|---|---|---|---|
| assets_ids | string[] | 否 | 需要接收事件的 asset ids（token IDs）；用于 `market` channel |
| markets | string[] | 否 | 需要接收事件的 market ids（condition IDs）；用于 `user` channel |
| operation | string | 是 | `"subscribe"` 或 `"unsubscribe"` |
| custom_feature_enabled | bool | 否 | 启用 / 禁用自定义功能 |

### 返回参数
本页未提供任何“返回/推送消息（events）”的结构与字段列表