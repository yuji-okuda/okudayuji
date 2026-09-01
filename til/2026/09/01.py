# 連想配列の基礎

## 基本の作り方
item = {
    "id": 101,
    "name": "Laptop",
    "price": 85000,
    "stock": 12
}

## 要素の取り出し（キーでアクセス）
print(item["name"])     # Laptop
print(item["price"])    # 85000
print(item.get("stock"))  # 12
