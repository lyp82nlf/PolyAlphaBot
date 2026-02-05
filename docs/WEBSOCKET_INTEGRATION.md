# Polymarket WebSocket 接入文档

> 版本: v1.0 | 更新时间: 2026-01-21 | 作者: PolyArb-Alpha

---

## 目录

1. [概述](#概述)
2. [WebSocket 端点](#websocket-端点)
3. [Market Channel (市场频道)](#market-channel-市场频道)
4. [User Channel (用户频道)](#user-channel-用户频道)
5. [认证机制](#认证机制)
6. [消息格式](#消息格式)
7. [连接管理](#连接管理)
8. [错误处理](#错误处理)
9. [最佳实践](#最佳实践)

---

## 概述

Polymarket 提供两个 WebSocket 频道用于实时数据推送:

| 频道 | 用途 | 认证要求 | 推送内容 |
|------|------|---------|---------|
| **Market Channel** | 市场数据 | ❌ 公开 | 订单簿、价格变化、成交价、Tick Size 等 |
| **User Channel** | 用户活动 | ✅ 需要 | 订单状态、成交记录 |

### 核心特性

- ⚡ **低延迟**: <100ms 实时推送
- 📊 **Level 2 数据**: 完整订单簿深度
- 🔄 **增量更新**: 只推送变化的数据
- 🔐 **安全认证**: User Channel 使用 API Key 认证

---

## WebSocket 端点

### 基础 URL

```
wss://ws-subscriptions-clob.polymarket.com
```

### 完整端点

| 频道 | 端点 | 说明 |
|------|------|------|
| Market | `wss://ws-subscriptions-clob.polymarket.com/ws/market` | 公开市场数据 |
| User | `wss://ws-subscriptions-clob.polymarket.com/ws/user` | 用户私有数据 |

---

## Market Channel (市场频道)

### 1. 连接流程

```python
import websocket
import json

# 1. 建立连接
ws = websocket.WebSocketApp(
    "wss://ws-subscriptions-clob.polymarket.com/ws/market",
    on_open=on_open,
    on_message=on_message,
    on_error=on_error,
    on_close=on_close
)

# 2. 连接成功后发送初始订阅
def on_open(ws):
    subscribe_msg = {
        "type": "market",
        "assets_ids": [
            "21742633143463906290569050155826241533067272736897614950488156847949938836455",
            "52114319501245915516055106046884209969926127482827954674443846427813813222426"
        ]
    }
    ws.send(json.dumps(subscribe_msg))
```

### 2. 订阅消息格式

#### 初始订阅 (连接后首次发送)

```json
{
  "type": "market",
  "assets_ids": [
    "token_id_1",
    "token_id_2"
  ]
}
```

#### 动态订阅 (运行中添加)

```json
{
  "operation": "subscribe",
  "assets_ids": [
    "new_token_id_1",
    "new_token_id_2"
  ]
}
```

#### 取消订阅

```json
{
  "operation": "unsubscribe",
  "assets_ids": [
    "token_id_to_remove"
  ]
}
```

### 3. 推送消息类型

#### 3.1 订单簿快照/更新 (`book`)

**触发时机**: 订阅成功后立即推送完整订单簿,后续增量更新

```json
{
  "event_type": "book",
  "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
  "market": "0x1234...",
  "timestamp": "1705824000000",
  "hash": "0xabc...",
  "bids": [
    {"price": "0.52", "size": "100.5"},
    {"price": "0.51", "size": "250.0"}
  ],
  "asks": [
    {"price": "0.53", "size": "150.0"},
    {"price": "0.54", "size": "200.0"}
  ]
}
```

**字段说明**:

| 字段 | 类型 | 说明 |
|------|------|------|
| `event_type` | string | 固定为 `"book"` |
| `asset_id` | string | Token ID |
| `market` | string | Condition ID (市场ID) |
| `timestamp` | string | Unix 时间戳 (毫秒) |
| `hash` | string | 订单簿哈希 (用于校验) |
| `bids` | array | 买单价格档位 (价格降序) |
| `asks` | array | 卖单价格档位 (价格升序) |

⚠️ **注意**: 文档中结构表使用 `buys`/`sells`,但实际响应使用 `bids`/`asks`

#### 3.2 价格档位变化 (`price_change`)

**触发时机**: 某个价格档位的数量发生变化

```json
{
  "event_type": "price_change",
  "market": "0x1234...",
  "timestamp": "1705824000000",
  "price_changes": [
    {
      "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
      "price": "0.52",
      "size": "120.5",
      "side": "BUY",
      "hash": "0xdef...",
      "best_bid": "0.52",
      "best_ask": "0.53"
    }
  ]
}
```

**字段说明**:

| 字段 | 类型 | 说明 |
|------|------|------|
| `price_changes` | array | 价格变化数组 |
| `asset_id` | string | Token ID |
| `price` | string | 变化的价格档位 |
| `size` | string | 该档位新的总数量 (0表示移除) |
| `side` | string | `"BUY"` 或 `"SELL"` |
| `best_bid` | string | 当前最优买价 |
| `best_ask` | string | 当前最优卖价 |

⚠️ **Breaking Change**: 该消息格式将在 **2025-09-15 23:00 UTC** 更新

#### 3.3 Tick Size 变化 (`tick_size_change`)

**触发时机**: 最小价格变动单位发生变化

```json
{
  "event_type": "tick_size_change",
  "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
  "market": "0x1234...",
  "old_tick_size": "0.01",
  "new_tick_size": "0.001",
  "side": "BUY",
  "timestamp": "1705824000000"
}
```

⚠️ **注意**: 文档结构表中 `event_type` 写为 `"price_change"`,但实际应为 `"tick_size_change"`

#### 3.4 最新成交价 (`last_trade_price`)

**触发时机**: 有新的成交发生

```json
{
  "event_type": "last_trade_price",
  "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
  "market": "0x1234...",
  "price": "0.525",
  "size": "50.0",
  "side": "BUY",
  "fee_rate_bps": "100",
  "timestamp": "1705824000000"
}
```

**字段说明**:

| 字段 | 类型 | 说明 |
|------|------|------|
| `price` | string | 成交价格 |
| `size` | string | 成交数量 |
| `side` | string | 成交方向 (`"BUY"` 或 `"SELL"`) |
| `fee_rate_bps` | string | 手续费率 (基点, 1 bps = 0.01%) |

#### 3.5 最优买卖价 (`best_bid_ask`)

**触发时机**: 最优买卖价发生变化

```json
{
  "event_type": "best_bid_ask",
  "market": "0x1234...",
  "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
  "best_bid": "0.52",
  "best_ask": "0.53",
  "spread": "0.01",
  "timestamp": "1705824000000"
}
```

⚠️ **注意**: 需要启用 `custom_feature_enabled` flag

#### 3.6 新市场创建 (`new_market`)

**触发时机**: 平台创建新市场

```json
{
  "event_type": "new_market",
  "id": "market_123",
  "question": "Will Bitcoin reach $100k in 2026?",
  "market": "0x1234...",
  "slug": "bitcoin-100k-2026",
  "description": "Market description...",
  "assets_ids": ["token_yes", "token_no"],
  "outcomes": ["Yes", "No"],
  "timestamp": "1705824000000",
  "event_message": {
    "id": "event_123",
    "ticker": "BTC",
    "slug": "bitcoin-event",
    "title": "Bitcoin Price Prediction",
    "description": "Event description..."
  }
}
```

⚠️ **注意**: 需要启用 `custom_feature_enabled` flag

#### 3.7 市场结算 (`market_resolved`)

**触发时机**: 市场结算完成

```json
{
  "event_type": "market_resolved",
  "id": "market_123",
  "question": "Will Bitcoin reach $100k in 2026?",
  "market": "0x1234...",
  "slug": "bitcoin-100k-2026",
  "description": "Market description...",
  "assets_ids": ["token_yes", "token_no"],
  "outcomes": ["Yes", "No"],
  "winning_asset_id": "token_yes",
  "winning_outcome": "Yes",
  "timestamp": "1705824000000",
  "event_message": {
    "id": "event_123",
    "ticker": "BTC",
    "slug": "bitcoin-event",
    "title": "Bitcoin Price Prediction",
    "description": "Event description..."
  }
}
```

---

## User Channel (用户频道)

### 1. 连接流程 (带认证)

```python
from py_clob_client.client import ClobClient

# 1. 初始化 CLOB Client 获取 API 凭证
client = ClobClient(
    host="https://clob.polymarket.com",
    key=PRIVATE_KEY,
    chain_id=137
)
api_creds = client.create_or_derive_api_creds()

# 2. 连接 User WebSocket
ws = websocket.WebSocketApp(
    "wss://ws-subscriptions-clob.polymarket.com/ws/user",
    on_open=on_open,
    on_message=on_message
)

# 3. 发送认证订阅消息
def on_open(ws):
    auth_msg = {
        "type": "user",
        "markets": [],  # 可选: 过滤特定市场
        "auth": {
            "apiKey": api_creds['apiKey'],
            "secret": api_creds['secret'],
            "passphrase": api_creds['passphrase']
        }
    }
    ws.send(json.dumps(auth_msg))
```

### 2. 认证消息格式

```json
{
  "type": "user",
  "markets": ["condition_id_1", "condition_id_2"],
  "auth": {
    "apiKey": "your_api_key",
    "secret": "your_api_secret",
    "passphrase": "your_passphrase"
  }
}
```

**字段说明**:

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `type` | string | ✅ | 固定为 `"user"` |
| `markets` | array | ❌ | 过滤特定市场 (可选,留空接收所有) |
| `auth` | object | ✅ | 认证信息 |
| `auth.apiKey` | string | ✅ | API Key |
| `auth.secret` | string | ✅ | API Secret |
| `auth.passphrase` | string | ✅ | API Passphrase |

### 3. 推送消息类型

#### 3.1 交易消息 (`trade`)

**触发时机**: 订单成交时

```json
{
  "event_type": "trade",
  "type": "TRADE",
  "id": "trade_123",
  "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
  "market": "0x1234...",
  "outcome": "Yes",
  "price": "0.525",
  "size": "50.0",
  "side": "BUY",
  "status": "MATCHED",
  "taker_order_id": "order_456",
  "matchtime": "1705824000000",
  "timestamp": "1705824000000",
  "last_update": "1705824000000",
  "owner": "api_key_owner",
  "trade_owner": "api_key_trade_owner",
  "maker_orders": [
    {
      "order_id": "order_789",
      "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
      "outcome": "Yes",
      "price": "0.525",
      "matched_amount": "25.0",
      "owner": "maker_api_key"
    }
  ]
}
```

**字段说明**:

| 字段 | 类型 | 说明 |
|------|------|------|
| `event_type` | string | 固定为 `"trade"` |
| `type` | string | 固定为 `"TRADE"` |
| `id` | string | 交易ID |
| `taker_order_id` | string | Taker 订单ID |
| `maker_orders` | array | Maker 订单详情数组 |
| `matchtime` | string | 撮合时间 (毫秒时间戳) |
| `status` | string | 交易状态 |

#### 3.2 订单消息 (`order`)

**触发时机**: 订单创建/更新/取消时

```json
{
  "event_type": "order",
  "type": "PLACEMENT",
  "id": "order_123",
  "asset_id": "21742633143463906290569050155826241533067272736897614950488156847949938836455",
  "market": "0x1234...",
  "outcome": "Yes",
  "price": "0.52",
  "side": "BUY",
  "original_size": "100.0",
  "size_matched": "25.0",
  "owner": "api_key_owner",
  "order_owner": "api_key_order_owner",
  "timestamp": "1705824000000",
  "associate_trades": ["trade_123", "trade_456"]
}
```

**字段说明**:

| 字段 | 类型 | 说明 |
|------|------|------|
| `event_type` | string | 固定为 `"order"` |
| `type` | string | `"PLACEMENT"` / `"UPDATE"` / `"CANCELLATION"` |
| `original_size` | string | 原始订单数量 |
| `size_matched` | string | 已成交数量 |
| `associate_trades` | array | 关联的交易ID列表 |

---

## 认证机制

### 获取 API 凭证

User Channel 需要使用 CLOB API 凭证进行认证:

```python
from py_clob_client.client import ClobClient

# 方式1: EOA 钱包 (直接使用私钥)
client = ClobClient(
    host="https://clob.polymarket.com",
    key="0x...",  # 私钥
    chain_id=137
)

# 方式2: Email/Magic 代理钱包
client = ClobClient(
    host="https://clob.polymarket.com",
    key="0x...",  # 私钥
    chain_id=137,
    signature_type=1,  # Email/Magic
    funder="0x..."  # 代理钱包地址
)

# 方式3: 浏览器钱包代理
client = ClobClient(
    host="https://clob.polymarket.com",
    key="0x...",
    chain_id=137,
    signature_type=2,  # 浏览器钱包
    funder="0x..."
)

# 生成/导出 API 凭证
api_creds = client.create_or_derive_api_creds()
print(api_creds)
# {
#   'apiKey': 'xxx',
#   'secret': 'xxx',
#   'passphrase': 'xxx'
# }
```

---

## 消息格式

### 通用规范

1. **所有消息均为 JSON 格式**
2. **数字字段使用字符串** (避免精度丢失)
3. **时间戳为毫秒级 Unix 时间戳字符串**
4. **价格/数量保留小数点后精度**

### 客户端发送消息类型

| 消息类型 | 用途 | 频道 |
|---------|------|------|
| 初始订阅 | 连接后首次订阅 | Market / User |
| 动态订阅 | 运行中添加订阅 | Market |
| 取消订阅 | 移除订阅 | Market |
| PING | 保活 | Market / User |

### 服务端推送消息类型

| 消息类型 | event_type | 频道 |
|---------|-----------|------|
| 订单簿 | `book` | Market |
| 价格变化 | `price_change` | Market |
| Tick Size 变化 | `tick_size_change` | Market |
| 最新成交价 | `last_trade_price` | Market |
| 最优买卖价 | `best_bid_ask` | Market |
| 新市场 | `new_market` | Market |
| 市场结算 | `market_resolved` | Market |
| 交易 | `trade` | User |
| 订单 | `order` | User |

---

## 连接管理

### 1. 心跳保活 (PING)

**建议间隔**: 每 10 秒发送一次

```python
import threading
import time

def send_ping(ws):
    while True:
        time.sleep(10)
        ws.send("PING")

# 启动心跳线程
ping_thread = threading.Thread(target=send_ping, args=(ws,), daemon=True)
ping_thread.start()
```

### 2. 断线重连

```python
def on_close(ws, close_status_code, close_msg):
    logger.warning(f"WebSocket 连接关闭: {close_status_code} - {close_msg}")
    logger.info("5秒后尝试重连...")
    time.sleep(5)
    reconnect()

def reconnect():
    global ws
    ws = websocket.WebSocketApp(
        "wss://ws-subscriptions-clob.polymarket.com/ws/market",
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()
```

### 3. 订阅状态管理

```python
class SubscriptionManager:
    def __init__(self):
        self.subscribed_assets = set()
    
    def add_subscription(self, ws, asset_ids):
        """添加订阅"""
        new_assets = [aid for aid in asset_ids if aid not in self.subscribed_assets]
        if new_assets:
            msg = {
                "operation": "subscribe",
                "assets_ids": new_assets
            }
            ws.send(json.dumps(msg))
            self.subscribed_assets.update(new_assets)
    
    def remove_subscription(self, ws, asset_ids):
        """取消订阅"""
        msg = {
            "operation": "unsubscribe",
            "assets_ids": asset_ids
        }
        ws.send(json.dumps(msg))
        self.subscribed_assets.difference_update(asset_ids)
```

---

## 错误处理

### 常见错误

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| 连接失败 | 网络问题 | 检查网络,实现重连机制 |
| 认证失败 | API 凭证错误 | 检查 apiKey/secret/passphrase |
| 订阅失败 | Token ID 不存在 | 验证 asset_id 有效性 |
| 消息解析失败 | JSON 格式错误 | 添加异常捕获 |

### 错误处理示例

```python
def on_error(ws, error):
    logger.error(f"WebSocket 错误: {error}")
    # 根据错误类型决定是否重连
    if isinstance(error, ConnectionError):
        reconnect()

def on_message(ws, message):
    try:
        data = json.loads(message)
        event_type = data.get('event_type')
        
        if event_type == 'book':
            handle_book_update(data)
        elif event_type == 'price_change':
            handle_price_change(data)
        # ... 其他消息类型
        
    except json.JSONDecodeError as e:
        logger.error(f"JSON 解析失败: {e}, 原始消息: {message}")
    except Exception as e:
        logger.error(f"消息处理异常: {e}")
```

---

## 最佳实践

### 1. 订阅管理

- ✅ **按需订阅**: 只订阅需要的 Token ID
- ✅ **动态调整**: 使用 subscribe/unsubscribe 动态管理
- ✅ **批量操作**: 一次订阅多个 Token 减少消息数
- ❌ **避免重复**: 订阅前检查是否已订阅

### 2. 消息处理

- ✅ **异步处理**: 使用队列或线程池处理消息
- ✅ **幂等性**: 处理逻辑应支持重复消息
- ✅ **快照+增量**: book 消息为快照,price_change 为增量
- ❌ **避免阻塞**: 不要在回调中执行耗时操作

### 3. 性能优化

```python
from queue import Queue
from threading import Thread

# 消息队列
message_queue = Queue()

def on_message(ws, message):
    # 快速入队,不阻塞接收
    message_queue.put(message)

def message_processor():
    """后台线程处理消息"""
    while True:
        message = message_queue.get()
        try:
            data = json.loads(message)
            # 处理逻辑...
        except Exception as e:
            logger.error(f"处理失败: {e}")
        finally:
            message_queue.task_done()

# 启动处理线程
processor = Thread(target=message_processor, daemon=True)
processor.start()
```

### 4. 数据一致性

```python
class OrderbookManager:
    def __init__(self):
        self.orderbooks = {}  # {asset_id: {bids: [], asks: []}}
    
    def handle_book(self, data):
        """处理完整订单簿快照"""
        asset_id = data['asset_id']
        self.orderbooks[asset_id] = {
            'bids': data['bids'],
            'asks': data['asks'],
            'hash': data['hash'],
            'timestamp': data['timestamp']
        }
    
    def handle_price_change(self, data):
        """处理增量价格变化"""
        for change in data['price_changes']:
            asset_id = change['asset_id']
            if asset_id not in self.orderbooks:
                # 缺少快照,请求重新订阅
                logger.warning(f"缺少 {asset_id} 的订单簿快照")
                continue
            
            # 更新对应价格档位
            side = 'bids' if change['side'] == 'BUY' else 'asks'
            price = change['price']
            size = change['size']
            
            # 移除旧档位
            self.orderbooks[asset_id][side] = [
                level for level in self.orderbooks[asset_id][side]
                if level['price'] != price
            ]
            
            # 添加新档位 (size > 0)
            if float(size) > 0:
                self.orderbooks[asset_id][side].append({
                    'price': price,
                    'size': size
                })
            
            # 重新排序
            self.orderbooks[asset_id][side].sort(
                key=lambda x: float(x['price']),
                reverse=(side == 'bids')
            )
```

### 5. 监控与日志

```python
import time
from collections import defaultdict

class WebSocketMonitor:
    def __init__(self):
        self.message_count = defaultdict(int)
        self.last_message_time = {}
        self.start_time = time.time()
    
    def record_message(self, event_type):
        self.message_count[event_type] += 1
        self.last_message_time[event_type] = time.time()
    
    def get_stats(self):
        uptime = time.time() - self.start_time
        return {
            'uptime_seconds': uptime,
            'message_count': dict(self.message_count),
            'messages_per_second': sum(self.message_count.values()) / uptime,
            'last_message_time': self.last_message_time
        }
    
    def check_health(self):
        """健康检查: 超过30秒没收到消息则告警"""
        now = time.time()
        for event_type, last_time in self.last_message_time.items():
            if now - last_time > 30:
                logger.warning(f"超过30秒未收到 {event_type} 消息")
                return False
        return True
```

---

## 附录: 完整示例代码

参见 `test_websocket_market.py` 和 `test_websocket_user.py`
