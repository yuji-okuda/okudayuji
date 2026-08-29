# 配列　リスト(list)のまとめ

## 基本の作り 
numbers = [1, 2, 3, 4]
fruits = ["apple", "banana", "orange"]
mixed = [1, "hello", True]


## 要素の取り出し（インデックス）
fruits = ["apple", "banana", "orange"]

print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # orange（末尾）


## 要素の追加
fruits = ["apple", "banana"]

fruits.append("orange")      # 末尾に追加
fruits.insert(1, "grape")    # 指定位置に追加


## 要素の削除
fruits = ["apple", "banana", "orange"]

fruits.remove("banana")  # 値を指定して削除
fruits.pop(0)            # インデックス指定で削除
fruits.pop()             # 末尾を削除


## 要素の変更
fruits = ["apple", "banana", "orange"]

fruits[1] = "grape"   # banana → grape に変更
