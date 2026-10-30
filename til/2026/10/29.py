# 関数まとめ
## len()
文字列の長さを取得する関数
product = "apple"
print(len(product))
5

## strip()
文字列の先頭と末尾の空白を削除する関数
text = "   python   "
print(text.strip())
python

## replace()
文字列を別の文字列に置換する関数
message = "I like coffee"
print(message.replace("coffee", "tea"))
I like tea

## zfill()
文字列の先頭を0で埋める関数
number = "25"
print(number.zfill(5))
00025

## find()
指定した文字列の位置を取得する関数　※カウントは0から開始する
text = "python programming"
print(text.find("programming"))
7
※存在しない場合　-1
