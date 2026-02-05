## 接口名称
WSS Authentication（WebSocket 鉴权 / 仅 user channel 需要鉴权）

## 请求方法
未在本页给出（WebSocket 连接/消息鉴权说明，不是 HTTP 接口）

## Endpoint（完整路径）
未在本页给出

## 请求参数
> 本页说明：Only connections to `user` channel require authentication.

| 字段名 | 类型 | 是否必填 | 说明 |
|---|---|---|---|
| apikey | string | 否（本页 Optional=Yes） | Polygon account’s CLOB api key |
| secret | string | 否（本页 Optional=Yes） | Polygon account’s CLOB api secret |
| passphrase | string | 否（本页 Optional=Yes） | Polygon account’s CLOB api passphrase |

## 返回参数
本页未提供任何返回参数/返回结构定义（无）