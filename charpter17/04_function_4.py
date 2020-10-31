# 可写函数说明
def changeme(list2):
    "修改传入的列表"
    list2.append([1, 2, 3, 4])
    print("函数内取值: ", list2)
    return


# 调用changeme函数
mylist = [10, 20, 30]
print("函数外取值: ", mylist)
changeme(mylist)
print("函数外取值: ", mylist)
