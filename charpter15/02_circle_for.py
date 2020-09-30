sites = ["Baidu", "Google", "Test", "Taobao"]
for site in sites:
    if site == "Test":
        print("Test教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
    print("完成循环!")

print('\n')

for i in range(5):
    print(i)
