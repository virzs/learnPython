num_int = 123
num_float = 1.23
num_str = '456'

# int 与 float 运算 会默认转换成浮点类型
# 在 python 中较低的数据类型会转为较高的数据类型，以避免数据丢失
num_new = num_int + num_float
# string 和 int 或 float 类型无法隐式转换
num_new2 = num_int + num_str

print("num_int", type(num_int))
print("num_float", type(num_float))
print("num_new", type(num_new))
print("num_new2", type(num_new2))
