var1 = 'Hello World!'
var2 = "Testing"
print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])

print('\n')

# 字符串更新
var1 = 'Hello World!'
print("已更新字符串 : ", var1[:6] + 'Test!')

print('\n')

# 字符串运算符
a = "Hello"
b = "Python"
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")
if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")
print(r'\n')
print(R'\n')

print('\n')

# 字符串格式化
print("我叫 %s 今年 %d 岁!" % ('小明', 10))

print('\n')

# 三引号
para_str = """这是一个多行字符串的实例 
多行字符串可以使用制表符 TAB ( \t )。 
也可以使用换行符 [ \n ]。 """
print(para_str)

print('\n')

# f-string
name = 'Test'
print('Hello %s' % name)
