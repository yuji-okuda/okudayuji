# while と continueの基礎

## 0〜9のうち、偶数だけをスキップして表示する例
num = 0

while num < 10:
    num += 1
    if num % 2 == 0:   # 偶数ならスキップ
        continue
    print(num)
