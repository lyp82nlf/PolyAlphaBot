## Get multiple order books summaries by request

### 请求方法
POST

### Endpoint
https://clob.polymarket.com/books

---

## 请求参数（Body | application/json）

> Body 为 **数组**（Array），最大长度：`500`

| 字段名 | 类型 | 必填 | 说明 |
|---|---|---:|---|
| body | array<object> | 是 | 请求体为对象数组（最大 500 条） |
| — token_id | string | 是 | Token 的唯一标识符（The unique identifier for the token） |
| — side | enum<string>（BUY / SELL） | 否 | 可选 side 参数（Optional side parameter for certain operations） |

---

## 返回参数（200 | application/json）

> 返回为 **数组**（Array），数组元素为订单簿摘要对象

| 字段名 | 类型 | 必填 | 说明 |
|---|---|---:|---|
| response | array<object> | 是 | 成功响应为对象数组 |
| — market | string | 是 | Market identifier |
| — asset_id | string | 是 | Asset identifier |
| — timestamp | string<date-time> | 是 | Timestamp of the order book snapshot |
| — hash | string | 是 | Hash of the order book state |
| — bids | object[] | 是 | Array of bid levels |
| — — price | string | 是 | Bid level price |
| — — size | string | 是 | Bid level size |
| — asks | object[] | 是 | Array of ask levels |
| — — price | string | 是 | Ask level price |
| — — size | string | 是 | Ask level size |
| — min_order_size | string | 是 | Minimum order size for this market |
| — tick_size | string | 是 | Minimum price increment |
| — neg_risk | boolean | 是 | Whether negative risk is enabled |