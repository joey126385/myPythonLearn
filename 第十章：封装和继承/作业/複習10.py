"""
A:私有化:
    一、甚麼是私有化
        在python 中，私有化是一種封裝的概念，用於限制對類的屬性和方法的訪問。
        私有化的目的是為了保護類的內部實現細節，防止外部代碼直接訪問和宿改類的私有成員。
    
    二、私有化語法
        變量或者方法 名字前面加上單底線或者雙底線 即 私有化




B:繼承:
    一、什麼是繼承
        1.當我們有一個基礎的類之後，如果說我需要使用這個類，基於他去進行升級，那麼可以使用繼承的概念。
        2.這個繼承概念是在編成裡面的一種實現方式，類似於生活中，複製一份新手機設計圖紙，再複製版的基礎上繼續修改。
        3.從父類中繼承(複製)來成員變量和成員方法(不含私有)。
    二、繼承的語法
        1.單繼承:
            class 類名(父類名):
                類代碼快
        2.多繼承 類名(父類名1,父類名2):
                代碼快
C:多繼承:
    一、什麼事多繼承?
        一個子類別可以繼承很多個父類別的東西
    二、繼承注意事項
        多繼承中如果父類有同名方法或者屬性，預設以繼承順序為優先級
        即先繼承的被保留，後繼承的被覆蓋
D:繼承重寫
    一、重寫概念
        1.子類別繼承父類別的成員屬性和方法後，如果對其不滿意，那麼可以進行覆寫
    二、注意
        1.依但覆寫父類別成員，那麼對想調用成員的時候，就會調用父寫後的新成員



"""
print(">>>>>")


class A_Phone():
    def __init__(self, brand, model):  # 初始化對象
        self.brand = brand
        self.model = model
        self.__volt = 3.9

    def suspend_model(self):
        print("開啟")
        self.__volt = 3.1
        print(f"-----當前運行電壓為:{self.__volt}")

    def __check(self):
        status = "電池狀態警告"
        if (self.__volt > 3):
            status = "電池狀態正常"
        return status

    def display_info(self):
        print(f"品牌:{self.brand}", f"型號:{self.model}", f"電池狀態:{self.__check()}")


def a():
    # 實例化
    A1 = A_Phone(brand="A_brand", model="A_model")
    print(A1.model, A1.brand, A1)
    A1.suspend_model()
    A1.display_info()


# a()

print("<<<<<")
"""
思考:
手机需要出新版本(新增功能) , 如果你是设计师,你会如何选择?
1.每一代新款手机,都从0开始出设计图 (从头写一个新的类)
2,基于老款的设计图,修修改改. (基于已有的Phone类代码进行修改)
"""
print(">>>>>")
# 父類別
class B_Phone():
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def make_call(self,phoneNumber):
        print(f"正在撥打電話{phoneNumber}")
#　子類別繼承　父類別
class B_Phone_Plus(B_Phone):
    def send_msg(self,phoneNumber,message):
        print(f"正在給號碼為{phoneNumber}  發送訊息{message}")
class B_Plus_Plus(B_Phone_Plus):
    def nfc(self):
        print(f"使用NFC功能")

# 2.0 版本
def b1():
    x1=B_Phone_Plus(brand="B牌子",price="1000")
    x1.make_call("000000000")
    x1.send_msg("111111",'help')

def b2():
    x1=B_Plus_Plus(brand="BB牌子",price="99")
    x1.make_call('12')
    x1.nfc()
    x1.send_msg("1111","mmsssggg")

# b2()

# b1()
print("<<<<<\n>>>>>")
class C_Phone():
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def make_call(self,phoneNumber):
        print(f"撥打電話{phoneNumber}")
    def use_nfc(self):
        print("NFC刷卡B")

class C_Nfc():
    def read_nfc(self):
        print("讀取NFC")
    def write(self):
        print("寫入")
    def use_nfc(self):
        print("NFC刷卡A")

class C_redLine():
    def control(self):
        print("正在遙控")

# 多繼承
class C_plus(C_Nfc,C_Phone,C_redLine):
    def send_msg(self,phoneNumber,msg):
        print(f"給號碼為{phoneNumber}, 送出訊息{msg}")
def c1():
    a1=C_plus("apple",9999)
    a1.make_call("222")
    a1.send_msg('2222','haha')
    a1.use_nfc()

# c1()
print("<<<<<\n>>>>>")

class D_phone():
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def make_call(self, phone_number):
        print(f"正在给号码为{phone_number}的机主打电话")
class D_plus(D_phone):
    def __init__(self, brand, price,msg):
        D_phone.__init__(self,brand, price)
        self.msg = msg
        print(self.msg)
    def send_msg(self, phoneNumber, msg):
        print(f"{phoneNumber}  {msg}")
    def make_call(self, phone_number):
        print("父寫.....")

def d1():
    x1=D_plus(brand="Ss",price="111",msg="1111")
    x1.make_call("aaaaaa")
    x1.send_msg(132,2)

d1()
"""
按照需求，完善该 手机类
练习1、
    现代智能手机通常使用锂离子电池作为电源，电池的标准工作电压约为3.7伏。
    当手机处于低功耗模式或待机状态时，电压可能略微降低到大约3.6伏；
    而在执行高强度运算、玩游戏或其他耗能较大的任务时，电压则可能升至接近4.2伏的高点。 
    需求一: 为手机类新增“运行电压私有属性”,私有属性初始值为3.7
    需求二: 当待机模式时,调整“运行电压私有属性”为3.6 
练习2、
    现代智能手机在使用中，我们通常能够查看手机的详细信息，
    信息包括 手机品牌、手机型号、电池电压、以及电池状态。
    需求一: 为手机类新增检查电池状态的私有方法（电池状态自定义）,电池运行电压>3则是正常,否则电池状态为不正常
    需求二: 完善查看手机详细信息的方法，实现能在查看手机详细信息时显示电池状态。
"""


class A_p_1():
    def __init__(self, model):
        self.model = model
        self.__battery = "3.7"
