#!/usr/bin/python3

test = 'Testing'

print(test)  # 输出字符串
print(test[0:-1])  # 输出第一个到倒数第二个的所有字符
print(test[0])  # 输出字符串第一个字符
print(test[2:5])  # 输出从第三个开始到第五个的字符
print(test[2:])  # 输出从第三个开始的后的所有字符
print(test * 2)  # 输出字符串两次，也可以写成 print (2 * test)
print(test + "TESTING")  # 连接字符串


print('Te\nst')
print(r'Te\nst')

word = 'Python'
print(word[0], word[5])
print(word[-1], word[-6])