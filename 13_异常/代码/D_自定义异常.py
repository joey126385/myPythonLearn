
"""
一、什么是异常类
   我们抛出的异常，在Python中，都是一个个具体的异常对象。
这些异常对象都是根据异常模版（异常类）产生的。

自定义异常 == 自定义异常类
注意：自定义异常类必须继承一个异常父类

二、自定义异常如何抛出使用？
   --> raise关键词 用于抛出指定异常
"""

# 练习：模拟登录功能中抛出异常功能
# 需求：登录的时候必须用户名要填写，否则抛出用户名不能为空异常
class MyError(Exception):
    # 初始化方法，用于设置当前异常对象的异常信息
    def __init__(self,msg):
        self.msg = msg

    # 用于在打印对象的时候返回字符串的方法
    def __str__(self):
        return self.msg


user_name = input("请输入用户名：")
if user_name=='' or user_name == None:
    x = MyError("用户名不能为空！")
    raise x   # 抛出异常
else:
    print("用户名正确！")


# 编程是一件自由度很高的事情，就像画画一样。Python给我们提供了很多功能，并不是每一个功能都是用到的多。





