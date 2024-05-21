"""
一、什么是多继承？
    一个儿子可以有多个父亲（一个子类可以继承很多个父类的东西）
二、继承注意事项？
    多继承中,如果父类有同名方法或者属性,默认以继承顺序为优先级.
即先继承的被保留,后继承的被覆盖.
"""

# 目前有三个设计图纸：

# 手机
# 设计手机模版，这个类是设计图纸 1.0   只能打电话
class Phone():
    # 初始化手机对象
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    # 模拟拨打电话
    def make_call(self, phone_number):
        print(f"正在给号码为{phone_number}的机主打电话")

# NFC读卡器
class Nfc():
    def read_nfc(self):
        print("读取nfc")
    def write_nfc(self):
        print("写入nfc")

# 红外线
class Hong():
    def control(self):
        print("正在遥控")


# 需求：设计一个升级版的 手机,拥有 手机，NFC，红外线功能