# 请解析以下分别是什么异常
"""
# KeyboardInterrupt  键盘终端异常（非常少见）
while True:
    print("hello world !")
"""



# 普通异常

"""
# FileNotFoundError  文件找不到异常
# 遇到该类问题：1、根据错误提示找到出现问题的代码。 2、结合提示信息，检查这行代码，及其上下两行代码。

with open('./月光--胡彦斌.mp3','rb')as f:
    x = f.read()
    print(x)
"""




"""
# NameError 名称错误
# 遇到该类问题：1、检查上下文代码是否存在申明该变量，如果申明的话，检查变量名是否正确
#            2、检查该内容，是否真的是一个变量还是应该值？
print(a)
"""




"""
# SyntaxError  语法错误
print("hello world !)
"""



      
      



"""
# TypeError 类型异常
x = input("请输入一个数字：")
if x%2==0:
    print("这是一个偶数")
else:
    print("这是一个奇数")
"""
