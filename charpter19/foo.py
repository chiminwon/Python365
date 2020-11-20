# f = open("SUService.log", "a")
# num = f.close('Python 1234567890\n12,1234567\n')
# print(num)

f = open("SUService.log", "r")

line_item = f.readline()
while line_item:
    print(line_item)
    line_item = f.readline()

# for x in f:
#     print(x, end ='')

f.close()
