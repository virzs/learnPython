# int(整数) float(浮点数) bool(布尔值) complex(复数)
# python3 中 bool 是 int 的子类，可以与数字相加。True == 1、False == 0 结果为 True，可以通过 is 判断类型

a, b, c, d = 1, 1.1, True, 1 + 3j

# 返回当前变量类型

print(type(a), type(b), type(c), type(d))

# 返回当前变量是否是某个类型

print(isinstance(a, int), isinstance(b, float), isinstance(c, bool),
      isinstance(d, complex))

# 运算

#加
print(5 + 4)

#减
print(4.2 - 3)

#乘
print(2 * 3)

# 除 输出浮点数
print(2 / 4)

#除 输出整数
print(2 // 4)

# 求余
print(2 % 1)

# 乘方
print(2**2)
