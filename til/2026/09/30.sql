# EXISTS を使用した UPDATE の例

UPDATE customers c
SET status = 'Y'
WHERE c.status IS NULL
  AND EXISTS (
      SELECT 1
      FROM orders o
      WHERE o.customer_id = c.customer_id
  );


## 処理内容

`customers` テーブルの `status` が `NULL` のデータのうち、`orders` テーブルに対応する注文情報が存在する顧客だけを更新します。

### 条件1：status が NULL

```sql
c.status IS NULL
```

まだステータスが設定されていない顧客だけを対象にします。

### 条件2：注文情報が存在する

```sql
EXISTS (
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
)
```

`orders` テーブルに同じ `customer_id` を持つデータが1件でも存在する場合に TRUE となります。

