"""
一、什么是多继承？
    一个儿子可以有多个父亲（一个子类可以继承很多个父类的东西）
二、继承注意事项？
    多继承中,如果父类有同名方法或者属性,默认以继承顺序为优先级.
即先继承的被保留,后继承的被覆盖。
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
    def nfc_shiyong(self):      # 手机1.0版本类中也有使用nfc的功能
        print("滴~正在使用NFC刷卡！","（当前手机1.0版）")

# NFC读卡器
class Nfc():
    def read_nfc(self):
        print("读取nfc")
    def write_nfc(self):
        print("写入nfc")
    def nfc_shiyong(self):      # NFC类中有使用nfc的功能
        print("滴~正在使用NFC刷卡！","（当前NFC版）")

# 红外线
class Hong():
    def control(self):
        print("正在遥控")


# 需求：设计一个升级版的 手机,拥有 手机1.0、NFC、红外线功能
class P_plus(Nfc,Phone,Hong):
    # pass      # pass用于补全代码，目前这个新的类，我们没有手动加任何功能
    # 创建一个模拟生活中发短信的方法
    def send_msg(self,phone_number,msg):
        print(f"正在给号码为{phone_number}的机主，发送信息：{msg}")


# 测试：
a1 = P_plus("苹果","8999")
# 测试是否具备1.0手机功能
a1.make_call("119")
# 测试是否具备 Nfc功能
a1.read_nfc()
# 测试是否具备 红外线功能
a1.control()
# 总结1：一个子类可以继承多个父类。
# 测试，我给子类新增功能后能否正常使用
a1.send_msg("119","嘿嘿，我在这!")
# 总结2：一个子类在继承多个父类后，不仅可以拥有父类的所有东西，还能够自己再加点功能。
# 测试，调用nfc使用功能【请问，这个nfc使用功能是手机1.0的？还是Nfc类的？】
a1.nfc_shiyong()
# 总结：在继承中，如果出现继承重复属性或者方法的情况，以第一个继承的为基准。