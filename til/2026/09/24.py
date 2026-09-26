# 変数の多重代入

name, age, city = "田中", 25, "広島"
print(name)  # 田中
print(age)   # 25
print(city)  # 広島

# 同じ値を複数の変数へ代入

x = y = z = 100
print(x)  # 100
print(y)  # 100
print(z)  # 100

# 変数の値を入れ替える

a = 10
b = 20
a, b = b, a
print(a) # 20
print(b) # 10
