def sum(a, b):
    # 计算a和b的和
    total = a + b
    print("自定义函数内 total = ", total)
    return total


x = 130
y = 245

total2 = sum(b=y, a=x)
print("主函数内 total2 = ", total2)
