# 基本数据类型
counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "test"  # 字符串

print(counter)
print(miles)
print(name)

print('-----------------------------------------------------------------')

# 多个变量赋值
a = b = c = 1
a, b, c = 1, 2, "test"

print('-----------------------------------------------------------------')

# 标准数据类型
# •	Number（数字）
# int、float、bool、complex
a, b, c, d = 20, 5.5, True, 4 + 3j
print(type(a), type(b), type(c), type(d))

a = 111
isinstance(a, int)

var1 = 1
var2 = 10
# 使用del语句删除一些对象引用
del var1

# •	String（字符串）
str = 'Testing'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次，也可以写成 print (2 * str)
print(str + "TESTING")  # 连接字符串

# •	List（列表）
list = ['abcd', 786, 2.23, 'test', 70.2]
tinylist = [123, 'test']

print(list)  # 输出完整列表
print(list[0])  # 输出列表第一个元素
print(list[1:3])  # 从第二个开始输出到第三个元素
print(list[2:])  # 输出从第三个元素开始的所有元素
print(tinylist * 2)  # 输出两次列表
print(list + tinylist)  # 连接列表


def reverseWords(input):
    # 通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords = input.split(" ")

    # 翻转字符串
    # 假设列表 list = [1,2,3,4],
    # list[0]=1, list[1]=2 ，而 -1 表示最后一个元素 list[-1]=4 ( 与 list[3]=4 一样)
    # inputWords[-1::-1] 有三个参数
    # 第一个参数 -1 表示最后一个元素
    # 第二个参数为空，表示移动到列表末尾
    # 第三个参数为步长，-1 表示逆向
    inputWords = inputWords[-1::-1]

    # 重新组合字符串
    output = ' '.join(inputWords)

    return output


if __name__ == "__main__":
    input = 'I like test'
    rw = reverseWords(input)
    print(rw)

# •	Tuple（元组）
tuple = ('abcd', 786, 2.23, 'test', 70.2)
tinytuple = (123, 'test')

print(tuple)  # 输出完整元组
print(tuple[0])  # 输出元组的第一个元素
print(tuple[1:3])  # 输出从第二个元素开始到第三个元素
print(tuple[2:])  # 输出从第三个元素开始的所有元素
print(tinytuple * 2)  # 输出两次元组
print(tuple + tinytuple)  # 连接元组

# •	Set（集合）
sites = {'Google', 'Taobao', 'Test', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)  # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Test' in sites:
    print('Test 在集合中')
else:
    print('Test 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(a - b)  # a 和 b 的差集
print(a | b)  # a 和 b 的并集
print(a & b)  # a 和 b 的交集
print(a ^ b)  # a 和 b 中不同时存在的元素

# •	Dictionary（字典）
dict = {}
dict['one'] = "1 - 教程"
dict[2] = "2 - 工具"
tinydict = {'name': 'test', 'code': 1, 'site': 'www.test.com'}
print(dict['one'])  # 输出键为 'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')
print('-----------------------------------------------------------------')
