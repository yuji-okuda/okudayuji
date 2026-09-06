# 連想配列の基礎

## 要素の追加・更新

item = {"id":101,"name":"Laptop","price":85000,"stock":12}

item["category"] = "PC"      # 追加
item["price"] = 82000        # 更新
item["stock"] += 3           # 更新（加算）

item.update({"color":"silver","stock":20})  # まとめて追加・更新
