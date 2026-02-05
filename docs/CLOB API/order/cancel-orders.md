# CLOB Orders — Cancel Orders

Source:
https://docs.polymarket.com/developers/CLOB/orders/cancel-orders

---

## Description

Cancels one or more existing orders on the Polymarket CLOB.

This endpoint allows clients to cancel orders by providing their order IDs.

---

## HTTP Request

Method:
POST

Path:
 /orders/cancel

---

## Authentication

This endpoint requires authentication.
Only orders belonging to the authenticated user can be cancelled.

---

## Request Body

### Request Body Fields

- order_ids (array of strings, required)
  List of order IDs to cancel.

---

## Example Request

{
  "order_ids": [
    "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
    "0xabc123..."
  ]
}

---

## Response

The response indicates the result of the cancellation request.

### Response Fields

- cancelled_order_ids (array of strings)
  List of order IDs that were successfully cancelled.

- failed_order_ids (array of strings)
  List of order IDs that could not be cancelled.

---

## Example Response

{
  "cancelled_order_ids": [
    "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b"
  ],
  "failed_order_ids": [
    "0xabc123..."
  ]
}

---

## Notes

- Orders that are already filled or cancelled cannot be cancelled again.
- Partial success is possible: some orders may cancel successfully while others fail.
- Clients should verify order status after cancellation using get-order or get-active-order.
