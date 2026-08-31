# 配列　リスト(tuple)のまとめ

## 基本の作り 
numbers = {1, 2, 3, 4}
fruits = {"apple", "banana", "orange"}
mixed = {1, "hello", True}

## 要素の取り出し（インデックス不可）
fruits[0]   # ❌ エラー

## 要素の追加
fruits = {"apple", "banana"}

fruits.add("orange")        # 1つ追加
fruits.update(["grape", "orange", "melon", "peach", "kiwi"])    # 複数追加（リストなど）

## 要素の削除
fruits = {"apple", "banana", "orange"}

fruits.remove("banana")  # 値を指定して削除（存在しないとエラー）
fruits.discard("banana") # 値を指定して削除（存在しなくてもOK）
fruits.pop()             # ランダムに1つ削除（順序なし）
fruits.clear()           # 全削除

## 集合演算
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # 和集合 → {1, 2, 3, 4, 5}
print(A & B)  # 積集合 → {3}
print(A - B)  # 差集合 → {1, 2}
print(A ^ B)  # 排他的論理和 → {1, 2, 4, 5}
