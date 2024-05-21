"""
A:認識類
    一、類定義語法:
        class 類名():
            屬性(在代碼中屬性用變量表示)
                    stu_Id = None
                    stu_Name = None
            行為(在代碼中行為用函數表示)

        *1:self 是我們在創建類行為時候的一個固定寫法，代表這個類對象本身。
        *2:python 中規定，在累中如果要訂用自身的屬性和行為，必須通過self去進行去使用
    二、注意:
        1.類名取名和編量名基本一致，只能由字母數字下划線開頭，不建議使用中文，但是首字母建議大寫
        2.類方法中一定會具備一個參數self
    三、如何使用類?
        1.語法 : 變量=類名()
    四、什麼是對象
        1.根據類別創建的實例，叫做對象。
B:面向對象
    一、為什麼要創建對象?什麼是面向對象?
        類只是一種程序內的【設計圖紙】，需要基於圖紙生產實體(對象)，才能正常工作，這種套路稱之為:面向對象編程
    二、什麼是面相對象?
        即，設計類，並基於類創建對象，並使用對象完成具體的工作，這樣的一個編程叫做面相對象編程。
    三、注意:
        面相對象是一個編程思想。
C:初始化方法
    一、什麼是初始化方法?
        1.在創建對象的時候，會自動執行。
        2.在創建對象的時候，將傳入參數自動傳遞給 __init__ () 方法使用
    二、注意事項
        1.購造方法名稱: __init__() ，千萬不要忘記init 前後都有兩個底線
        2.購照方法也是成員方法，不要忘記在參數列表中提供self
        3.構造方法內定義成員便量，需要使用self 關鍵字。(成員變量通過self 使用)
    三、語法格式:
        def __init__ (self,屬性1,屬性2...)
            self.屬性1=屬性1
            self.屬性2=屬性2
            ...
D:認識類案例升級
# 0、基于认识类的案例
# 1、通过控制台录入学生信息
# 2、将录入的信息储存在对象
# 3、将对象储存在一个序列中，实现能够存储多个学生对象，并且可以存储每个学生对应的每个信息
# 4、由于只有以上步骤的话，该程序只能录入一个学员信息，这样写意义不大，为了加强功能，我们加个循环，实现可以批量录入
# 5、由于现实使用过程中，信息录入是有次数的，所以我们加一个是否结束录入的询问，如果客户确定结束就停止录入，并打印已经录入的学生信息
E:認識類案例升級再升級
"""
print(">>>>>")
class A1(): # 命名 首字為大寫
    # 屬性(類變量/成員變量)
    stu_Id = None
    stu_Name = None

    def study (self,time):
        print(f"正在學習中，{time}分鐘後下課")
    def sleep(self):
        print("進入睡覺")

a1 = A1()
a1.stu_Id = 1
a1.stu_Name = "張三"
print(a1,a1.stu_Id,a1.stu_Name,a1.study(77),a1.sleep())
print("<<<<<")

#　Ｂ
print(">>>>>")
class B1():
    ID , Price = None, None
    def bell(self):
        import winsound
        winsound.Beep(400,1000)
b1=B1()

# b1.bell()
print("<<<<<")

#　Ｃ
print(">>>>>")
class C1():
    def __init__(self,ID,price):
        self.ID=ID
        self.price=price
        print("測試，對象在創建的時候是否會自動執行")
c1=C1(price=20,ID=20)
print(f"鬧鐘的編號{c1.ID},鬧鐘的價格{c1.price}")
print("<<<<<")
"""
# 0、基于【认识类】的案例
# 1、通过控制台录入学生信息
# 2、将录入的信息储存在对象
# 3、将对象储存在一个序列中，实现能够存储多个学生对象，并且可以存储每个学生对应的每个信息
# 4、由于只有以上步骤的话，该程序只能录入一个学员信息，这样写意义不大，为了加强功能，我们加个循环，实现可以批量录入
# 5、由于现实使用过程中，信息录入是有次数的，所以我们加一个是否结束录入的询问，如果客户确定结束就停止录入，并打印已经录入的学生信息
"""
print(">>>>>")
class Strudents ():
    stu_Id,stu_Name=None,None
    def __init__(self,stu_Id,stu_Name):
        self.stu_Id = stu_Id
        self.stu_Name = stu_Name
        print(f"學生 id -{stu_Id} 學生名字 {stu_Name}")
studentList = list()   #容器
def d1():

    while True:
        s_id = input("輸入學生編號")
        s_name = input("輸入學生姓名")
        s = Strudents(stu_Id=s_id, stu_Name=s_name)
        studentList.append(s)
        if (input("请问是否继续，继续扣q，其他结束：")=="q"):
          break
    print(studentList)

d1();
print("<<<<<")

"""
# 0、基于认识类的升级案例
# 1、通过控制台录入部分学生信息，其中学员id是程序自动生成
# 2、将录入的信息储存在对象中
# 3、将对象储存在一个序列中【该对象够存储多个学生对象，并且每个对象会存储学生对应的信息】
# 4、实现在录入且存储完一个学员信息之后，询问是否继续录入
"""

def e1():
    studentList2 = list()  # 容器
    auto_id = 0
    while True:
        s_name = input("輸入學生姓名")
        s=Strudents(stu_Id=auto_id+1,stu_Name=s_name)
        studentList.append(s)
        if (input("请问是否继续，继续扣q，其他结束：")=="q"):
          break
e1();
for data in studentList:
    print(data.stu_Id,data.stu_Name)
print("<<<<<")