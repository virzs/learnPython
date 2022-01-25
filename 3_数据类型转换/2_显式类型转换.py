# int() 强制转换为整型

x = int(1)

y = int(2.8)

z = int('3')

print(x, y, z)

# float() 强制转换成浮点型

x = float(1)

y = float(2.8)

z = float('3')

w = float('3.2')

print(x, y, z, w)

# str() 强制转换成字符串类型

x = str('s1')

y = str(2)

z = str(3.0)

print(x, y, z)

# 转为整数
print(int('1'))

# 转为浮点数
print(float('1.11'))

# 创建一个复数
print(complex(1))

# 将对象转为字符串
print(str({'arr': 1}))
print(str(1))

# 将对象转为表达式字符串
print(repr('1'))

# 计算字符串中有效的表达式
print(eval('pow(2,2)'))

# 将序列转为元组
print(tuple(['Google', 'Baidu']))

# 将序列转为列表
print(list(('Google', 'Taobao')))

# 转换为可变集合
print(set('google'))

# 创建一个字典。d 必须是一个 (key, value)元组序列。
print(dict(a=1, b=2, c=3))

print(dict([('one', 1), ('two', 2)]))

# 转换为不可变集合
print(frozenset(range(10)))
