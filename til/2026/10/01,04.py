# datetimeの基本

from datetime import datetime
now = datetime.now()
print(now)

print(now.year) # 年
print(now.month) # 月
print(now.day) # 日
 
print(now.hour) # 時
print(now.minute) # 分
print(now.second) # 秒

## 今日の日付の取得

from datetime import date
today = date.today()
 
print(today)
2026-10-01


## 特定の日付を作成

from datetime import datetime
birthday = datetime(1990, 5, 10)
 
print(birthday)
1990-05-10 00:00:00

## 日付のフォーマット変換

from datetime import datetime
now = datetime.now()
 
print(now.strftime("%Y/%m/%d"))
2026/10/01
