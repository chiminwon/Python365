# import 与 from...import
# 导入 sys 模块
import sys

print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
    print('\n python 路径为', sys.path)