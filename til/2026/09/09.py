# for＋breakの基礎

nums = [1, 2, 3, 4, 5]   # リストを用意
for n in nums:           # 要素を順番に取り出す
    if n == 3:           # 条件に一致したら
        break            # ループを中断する
    print(n)             # 3が出る前の値だけ表示される
