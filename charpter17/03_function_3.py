def change(b):
    print(id(b))
    # 指向的是同一个对象
    b = 10
    print(id(b))


# 一个新对象
a = 1
print(id(a))
change(a)
print(id(a))
