# int(整数) float(浮点数) bool(布尔值) complex(复数)
# python3 中 bool 是 int 的子类，可以与数字相加。True == 1、False == 0 结果为 True，可以通过 is 判断类型

a, b, c, d = 1, 1.1, True, 1 + 3j

# 返回当前变量类型

print(type(a), type(b), type(c), type(d))

# 返回当前变量是否是某个类型

print(isinstance(a, int), isinstance(b, float), isinstance(c, bool),
      isinstance(d, complex))
