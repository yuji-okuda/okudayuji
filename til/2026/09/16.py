# 複数テーブルの結合

customers — 顧客情報
orders — 注文情報
order_items — 注文内の商品
products — 商品情報

顧客（customers）を起点にすべての情報を取得
顧客に紐づく 注文（orders） を結合
注文に紐づく 注文商品（order_items） を結合
注文商品に紐づく 商品情報（products） を結合
商品 × 数量 で 合計金額（total_price） を計算
LEFT JOIN のため、注文がない顧客も表示される

SELECT
    c.customer_id,
    c.customer_name,
    o.order_id,
    o.order_date,
    p.product_name,
    oi.quantity,
    (oi.quantity * p.price) AS total_price
FROM customers AS c
LEFT JOIN orders AS o
    ON c.customer_id = o.customer_id
LEFT JOIN order_items AS oi
    ON o.order_id = oi.order_id
LEFT JOIN products AS p
    ON oi.product_id = p.product_id
ORDER BY c.customer_id, o.order_id;
