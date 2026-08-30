# 配列　リスト(tuple)のまとめ

## 基本の作り 
numbers = (1, 2, 3, 4)
fruits = ("apple", "banana", "orange")
mixed = (1, "hello", True)

## 要素の取り出し（インデックス）
fruits = ("apple", "banana", "orange")

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # orange（末尾）

## ⚠️ タプルは「変更不可」
fruits = ("apple", "banana")

fruits.append("orange")      # ❌ エラー
fruits.insert(1, "grape")    # ❌ エラー
fruits.remove("banana")      # ❌ エラー
fruits.pop()                 # ❌ エラー
fruits[1] = "grape"          # ❌ エラー
