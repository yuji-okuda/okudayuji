# bool型を使ったif文の例

is_logged_in = True  # bool型(True または False)

if is_logged_in:
    print("ログイン済みです")
else:
    print("ログインしてください")

bool()を使用すると、()内のデータによって、True　か　False が返される
・1、-100 → True
・0 → False

・[1] → True
・[] → False

・None → False
・"" → False

・"boo" → True
