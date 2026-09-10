# for＋continue

nums = [1, 2, 3, 4, 5]   # リストを用意
for n in nums:           # 要素を順番に取り出す
    if n == 3:           # 条件に一致したら
        continue         # 3 のときだけ処理をスキップ
    print(n)             # 3 以外の値だけ表示される
