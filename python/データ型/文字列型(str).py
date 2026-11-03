#　文字列の連結

print("今日の曜日は" + "水曜日")
print("明日の曜日は" "木曜日")

#　文字列と数値を連結したい場合
#  star()関数で数値を文字列に変換する

print("次の会議は、" + star(15) + "日")

# 同じ文字列を連結したい場合
print("プログラミング" * 5)

# 上記と同じ
print("プログラミング" + "プログラミング" + "プログラミング" + "プログラミング" + "プログラミング")

# 変数を使って出力

user_name = "太郎"
print(user_name)

# 変数の中身は入れ替える事が可能

user_name = "次郎"
print(user_name)

# 変数による整数型と不動型の計算は可能

number1 = 3
number2 = 0.5
print(number1 + number2)

# 変数による文字列型の連結は可能

last_name = "オクダ"
first_name = "ユウジ"
print(last_name + first_name)

# 文字列の中で変数の中身を表示させる方法
# (文字列の直前にfをつけ、変数を{}で囲う)

last_name = "山田"
first_name = "太郎"
sister_name = "花子"

print(f"私の名前は{last_name}{first_name}です。妹の名前は{last_name}{sister_name}です。")
