def print_func(par):
    print("Hello : ", par)
    return


def print_func2(par):
    print("Hello : ", par)
    return


def sum(a, b):
    # 计算a和b的和
    total = a + b
    print("自定义函数内 total = ", total)
    return total


if __name__ == '__main__':
    print(44 + 99)
    print('程序自身在运行')
else:
    print('我来自另一模块')
