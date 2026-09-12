# while + break の基礎
num = 0

while num < 10:
    if num == 5:
        print("5になったのでループ終了")
        break
    print(num)
    num += 1
