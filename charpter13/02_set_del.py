thisset = set(("Google", "Test", "Taobao"))
thisset.remove("Taobao")
print(thisset)
{'Google', 'Test'}
thisset.remove("Facebook")

# thisset = set(("Google", "Test", "Taobao"))
# thisset.discard("Google")  # 不存在不会发生错误
# print(thisset)
# thisset.discard("Facebook")  # 不存在不会发生错误
# print(thisset)
# {'Taobao', 'Google', 'Test'}
