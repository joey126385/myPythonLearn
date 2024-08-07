"""
1、继承重写概念：
子类继承父类的成员属性和方法后，如果对其不满意，那么可以进行复写。
即：在子类中重新定义同名的属性方法即可。

2、注意：
   一旦复写父类成员，那么类对象调用成员的时候，就会调用复写后的新成员。
如果需要使用被复写的父类成员，需要特殊的调用方式。
（只能在子类内部调用父类的同名成员，子类的实体类对象调用默认是调用子类复写）
"""

# 设计手机模版，这个类是设计图纸 1.0   只能打电话
class Phone():
    # 初始化手机对象
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    # 模拟拨打电话
    def make_call(self, phone_number):
        print(f"正在给号码为{phone_number}的机主打电话")

# 手机模版 2.0   加了一个发短信的功能，并增加打电话功能为5G电话。
