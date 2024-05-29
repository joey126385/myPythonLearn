"""
A:魔法方法
    一、什麼是魔法方法
        1.魔法方法名稱前後都有兩個底線 例   __init__ 、__new__ 、__del__ 、__str__
        2.無須自己手動調用，他會自動執行。
    二、常見的魔法方法??
        1.  __init__()  :   初始化方法，用來初始化當前實力對象屬性值。
        2.  __new__()   :   構照方法，用來構照創建一個實例對象
        3.  __del__()   :   當打印對象的時候返回，對象的字串內容 自定義
        4.  __str__()   :   析構方法，在對向被銷毀的自動調用。
    三、一個類別在實例畫對象時，python 做了哪些動作
        1.  python 會調用該類別中的 new 方法去創建一個對象
        2.  python 會調用該類別中的 init方法，獲取剛剛new 創建的對象，並進行初始化
        3.  最終，init 方法會返回創建好的，且初始化好的對象讓程序元進行保存。

B:裝飾器
    一、什麼是裝飾器
        1.裝飾器其實是一個閉包，其功能就是在不改動目標函數的同時，加額外的功能。
            閉包(是函數特殊的書寫狀態):
                (1)兩個函數嵌套
                (2)外層函數返回內層函數名(函數引用)
    二、閉包優勢
        1.能夠保護數據不被隨意修改
        2.閉包這樣的寫法可以延長，局部變量數據的使用壽命
        3.閉包可以用作裝飾器
    三、步驟
        1.  確定要升級的函數
        2.  寫一個閉包，在外層函數中，要有一個形參，用於接收要升級的函數
            而內層函數，用於實現具體的功能升級代碼
        3.  在需要升級的函數前面，加上   @　　裝飾器的名字
    四、範例
        1.閉包
    def B_f1(x):
        def action():
            x()
            return "動作"
        return  action
# 方式一
    def B_f2():
        print("sleeping")
    a=B_f1(B_f2)()
    print(a)
    print("----")
    @B_f1
    def B_f3():
        print("sleeping  333")
"""
class A_Cat1():

    # (1)
    def __init__(self , name , age: int):
        self.name = name
        self.age = age
        print(f"__init__  {name} \t {age}")

    def __new__(cls, *args, **kwargs):
        print(f"__new__")
        return super().__new__(cls)

    def __str__(self):
        print("__str__")
        return  f"__str__ 調用回傳 的name{self.name}  +**++ age {self.age}"

    def __del__(self):
        print("__del__")


# 實例化
print(">>>>> A")
a1=A_Cat1("n1","a1")
print(a1) #　回傳 __str__
print("<<<<<")

print(">>>>> B")

# 閉包
def B_func1():
    def B_func2():
        userName="jj"
        userPass="123"
        return userName+userPass
    return B_func2
print(f" 測試 B_func1 閉包  {B_func1()}\n{B_func1()()}")


def B_f1(x):
    def action():
        x()
        return "動作"
    return  action
# 方式一
def B_f2():
    print("sleeping")
a=B_f1(B_f2)()
print(a)
print("----")

# 裝飾器
@B_f1
def B_f3():
    print("sleeping  333")
B_f3()

print("<<<<<")

