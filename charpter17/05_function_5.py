# 关键字参数
def printme(str):
    "打印任何传入的字符串"
    print(str)
    return


# 调用printme函数
printme("Test教程")


# 可写函数说明
def printinfo(name, age):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo("test", 50)
printinfo(age=50, name="test")
printinfo(name="test", age=50)
