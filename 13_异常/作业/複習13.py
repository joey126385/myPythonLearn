"""
A:復現異常
    1.KeyboardInterrupt :   鍵盤終端異常  Ctrl + C  停止
    2.FileNotFoundError :   文件找不到
    3.NameError         :   名稱錯誤
    4.SyntaxError       :   語法錯誤
    5.TypeError         :   類型錯誤
    6.ValueError        :   當用戶輸入非數字的時候，出現值錯誤
    7.ZeroDivisionError :   除數不能是0
B:異常捕捉
    一、捕捉異常的語法:
        try:
            可能會發生異常的代碼
        except  [   異常類 as 別名   ]:
            發生異常的解決方案
        [else:
            沒有異常發生時執行的代碼]
        [finally:
            不管用沒有異常都會執行]
    二、解析:
        1.try       :告訴解釋器，這後面的代碼塊是可能發生異常的代碼塊
        2.except    :用於告訴解釋器，這裡是捕獲異常的，已經捕獲之後五里異常的。
        3.else      :當沒有發生異常的情況，執行的代碼塊
        4.finally   :不管用沒有異常都會進入，並執行其中的代碼。

C:異常傳遞
D:自訂義異常
    一、甚麼是異常類:
        1.
        2.
    二、自訂義異常如何拋出使用?
        1.  raise 關鍵詞   用於拋出指定異常
"""
class A_13():
    def __KeyboardInterrupt(self):
        while True:
            print("helloworld")
    def __FileNotFoundError(self):
        with open('./月光--胡彦斌.mp3','rb')as f:
            print(f.read())
    def __TypeError(self):
        x = input("请输入一个数字：")
        if x % 2 == 0:
            print("这是一个偶数")
        else:
            print("这是一个奇数")

    def run(self,m):
        # x = self.m
        if( m==0):
            self.__KeyboardInterrupt()
        elif(m==1):
            self.__FileNotFoundError()
        elif(m==2):
            self.__TypeError()
# A_13().run(2)
class B_13():
    def __ValueError(self):
        try:
            x=int(input("輸入數字"))
            if(x%2==0):
                print("偶數")
            else:
                print("奇數")
        except ValueError as e: # 指定抓取錯誤
            print(f"數入 非數字   {e}")

    def __ZeroDivisionError(self):
        try:
            x = int(input("第一個數字："))
            y = int(input("第二個數字："))
            if y % 2 == 0:  # 判断是否是偶数
                print(f"{y}是一个偶數。{x}/{y}={x / y}")
            else:
                print(f"{y}是一个奇數。{x}/{y}={x / y}")
        except Exception as e:  # 捕获所有异常，并获取具体的异常提示信息
            print(f"當前代碼 異常:{e}")

    def useElseFinally(self):
        try:
            print("try")
        except:
            print("except")
        else:
            print("else")
        finally:
            print("finally")

    def run(self,m):
        if(m==0):
            self.__ValueError()
        elif(m==1):
            self.__ZeroDivisionError()
        elif(m==2):
            self.useElseFinally()
# B_13().run(2)
class C_13():
    def func(self):
        def func01():
            print("這是func01 開始")

            try:
                num=1/0
            except Exception as e :
                print(f"當前異常 {e}")
            print("這是func01結束")

        def func02():
            print("這是func02開始")
            func01()
            print("這是func02結束")

        func02()
# C_13().func()
class D_13_MyError(Exception):

        def __init__(self,msg):
            self.msg=msg
        def __str__(self):
            return  self.msg

user_name = input("輸入名字")
if (user_name == '' or user_name == None):
    xx = D_13_MyError("用戶不存在")
    raise xx
else:
    print("輸入正確")

