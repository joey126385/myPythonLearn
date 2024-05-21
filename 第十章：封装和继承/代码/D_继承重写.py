"""
1、继承重写概念：
子类继承父类的成员属性和方法后，如果对其不满意，那么可以进行复写。
即：在子类中重新定义同名的属性方法即可。

2、注意：
   一旦复写父类成员，那么类对象调用成员的时候，就会调用复写后的新成员。
如果需要使用被复写的父类成员，需要特殊的调用方式。
（只能在子类内部调用父类的同名成员，子类的实体类对象调用默认是调用子类复写）
   某些情况下，在重写方法的时候，可能父类中的部分功能可以继续使用，
   这个时候，可以在的子类中调用父类的方法，可以减轻我们的编码负担。
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
class P_plus(Phone):
    # 新加功能：2.0手机要加一个新的属性，手机详情介绍。
    def __init__(self, brand, price,p_msg):     # 重写1.0的初始化方法
        # 在重写的子类中调用父类的方法，可以减轻我们的编码负担
        Phone.__init__(self,brand, price)
        self.p_msg = p_msg
        print(self.p_msg)

    # 创建一个模拟生活中发短信的方法
    def send_msg(self,phone_number,msg):
        print(f"正在给号码为{phone_number}的机主，发送信息：{msg}")

    # 重写：重新写一次。注意：子类重写父类的过程中，方法名要一样。子类重新父类方法后，再调用的话，就是调用重新后的内容。
    # 重写继承父类的方法
    def make_call(self, phone_number):
        print(f"5G通讯中.......正在给号码为{phone_number}的机主打电话")

# 创建一个2.0手机对象
n1 = P_plus("诺基亚","599","诺基亚手机质量嘎嘎嘎好！")
# 测试能否使用重写后的打电话功能
n1.make_call("12345")
# 测试能够使用2.0发短信新功能
n1.send_msg("12345","我举报！")