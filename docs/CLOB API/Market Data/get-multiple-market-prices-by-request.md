## 接口名称
Get multiple market prices by request  [oai_citation:0‡Polymarket](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request)

## 请求方法
POST  [oai_citation:1‡Polymarket](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request)

## Endpoint（完整路径）
https://clob.polymarket.com/prices  [oai_citation:2‡Polymarket](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request)

## 请求参数
> Body: `application/json`  
> 类型：`array`（Maximum array length: `500`）  [oai_citation:3‡Polymarket](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request)

| 字段名 | 类型 | 是否必填 | 说明 |
|---|---|---|---|
| (body) | array | 是 | 请求体为数组（最大长度 500）  [oai_citation:4‡Polymarket](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request) |
| — token_id | string | 是 | The unique identifier for the token  [oai_citation:5‡Polymarket](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request) |
| — side | enum&lt;string&gt; | 是 | The side of the market (BUY or SELL)  [oai_citation:6‡Polymarket](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request) |

**side 可选值**：`BUY`、`SELL`  [oai_citation:7‡Polymarket](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request)

## 返回参数
> 200 `application/json`（Successful response）  [oai_citation:8‡Polymarket](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request)  
> 描述：Map of token_id to side to price  [oai_citation:9‡Polymarket](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request)

| 字段名 | 类型 | 说明 |
|---|---|---|
| (root) | object | 返回对象：键为 `token_id`；值为该 token 的价格映射（side → price）  [oai_citation:10‡Polymarket](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request) |
| — {token_id} | object | 动态键：某个 token_id 对应的对象  [oai_citation:11‡Polymarket](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request) |
| — — BUY | string | BUY 方向价格（示例：`"1800.50"`）  [oai_citation:12‡Polymarket](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request) |
| — — SELL | string | SELL 方向价格（示例：`"1801.00"`）  [oai_citation:13‡Polymarket](https://docs.polymarket.com/api-reference/pricing/get-multiple-market-prices-by-request) |


response example:

```json
{
  "1234567890": {
    "BUY": "1800.50",
    "SELL": "1801.00"
  },
  "0987654321": {
    "BUY": "50.25",
    "SELL": "50.30"
  }
}
```