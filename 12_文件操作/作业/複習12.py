"""
A:普通文件操作
     一、文件操作指的是什麼操作
        1.針對余具體的某一個文件，進行讀取數據和寫入數據的操作
     二、如何進行讀寫操作
        1.python :使用 open() 函數方法，可以根據指定文件標識符來打開文件。
        2.語法:
            open (file ,model ,encoding )
                (1)file     要操作的是哪個文件?這個參數要一定要寫上文件格式，可以寫上文件地址
                (2)model    文件操作模式【只寫、只讀、追加、讀寫...】
                (3)encoding 編碼格式
     三、注意
        1.  open    函數是具有返回值的，他會返回打開的文件對象
        2.  open    函數打開一個文件後，如果我們不需要對該文件對象進行操作之後，
                    應該把這個文件關閉掉，以免防止資源被占用。
        3.  如果說當前文件操作已經進行玩了，一定要關閉操作對象，
            因為在項目裡面不可能只打開一個文件，如果一直不關閉的話會非常消耗電腦資源。
        4.  被操作的文件，原本是以什麼樣的編碼規則創建的，打開的時候就得以什麼編碼規則打開。
     四、路徑
        1.  絕對路徑    :  D:\pythonWork\
        2.  相對路徑    :
            (1) .   (代表當前文件本身)
            (2) ./  (代表當前文件旁邊)
     五、指針
        在使用open對文彥操作的過程中，
        其實，文件在近程讀取的時候，是一個小指針的，這個指針有點類似於老是唱片機的指針。
        文件讀取的原理，其實是，根據這個指針去移動讀取數據，文件在以指讀取模式剛打開的時候，者個指針是在文件開頭位置的，
        當文件數據讀取完，文件指真會移動到文件末尾。

        1.  .seek(指針位置) :修改指針位置函數
            .seel(0) -->調整文件指針為0

     六、文件操作模式
        1.  w   :   只寫
            以【只寫】模式打開文件。
                (1) 如果文件不存在，則根據指定文件名稱創建相應的文件
                (2) 如果文件已存在，則會覆蓋原來文件
        2.  r   :   只讀
            以【只讀】模式打開文件
                (1)如果指定文件不存在，則會出現(FileNotFoundError）。
                (2)預設默認情況下【指針】指向文件開頭。
        3.  a   :   追加
            以【追加】模型打開文件
                (1) 如果文件已存在，文件指針指向文件尾部，將內容追加在原文件後面。
                (2) 如果文件不存在，則會新建文件寫入內容。
        4.  a+  :   追加+讀取
            打開文件並允許更些(可讀可寫)
                (1) 如果文件已存在，文件指針會指向文件尾部
                (2) 將內容追加在原文件後面，如果文件不存在，則會新建文件且寫入內容
        5.  w+  :   寫入+讀取
        6.  r+  :   讀取+寫入
B:普通文件操作升級
    一、什麼是上下文管理
    二上下文管理文件讀寫與法
        with  open(filePath,model,) as 變數名:
            變量名.文件操作
C:媒體文件操作
    一、如何對媒體文件(圖片、視頻、音頻)進行操作?
        1.  rb  :   二進制只讀
        2.  wb  :   二進制只寫
        3.  ab  :   二進制追加
    二、詳細介紹?
        1.【 rb】 :   以二進制模式讀取文件。如果文件存在則馬上打開，如果文件不存在則報錯。
        2.【 wb】 :   以二進制模式寫入文件。文件不存在，會自己創建，文件已經存在，會覆蓋原文件。
        3.【 ab】 :   以二進制模式追加數據到文件末尾。文件存在則直接追加到之前的數據後面。文件不存在則創建一個文件並將數據寫入
D:os 庫
    一、  import os
    二、  函數:
    三、  模塊：
    四、  包:

"""
import os


class A_12():


    def __file_w(self):
        # 1.先打開這個文件 並告訴此文件是使用哪個模式
        w=open("./這是我創建的文件.txt","w",encoding="UTF-8")
        # print(w)
        # 2. 寫入文件
        w.write("海可哭")
        w.close()

    def __file_r(self):
        r=open("./這是我創建的文件.txt","r",encoding="UTF-8")
        print(f"查看讀文件前指針位置{r.tell()}")
        print(f"讀取文件內容\t{r.read()}")
        print(f"查看讀取文件後指針位置{r.tell()}")
        print(f"讀取文件未調整指針內容\t{r.read()}")
        r.seek(0)
        print(f"讀取文件調整指針後的內容\t{r.read()}")
        r.close()

    def __file_a(self):
        file=open("這是我創建的文件.txt","a",encoding="utf-8")
        print(f"當前文件指針為指{file.tell()}")
        file.write("石可爛")
        print(f"當前文件指針為指{file.tell()}")
        file.close()

    def run12(self,model):
        if(model==1):
            self.__file_w();
        elif (model==2):
            self.__file_r()
        elif (model==3):
            self.__file_a()
# A_12().run12(3)
print(">>>>>")
class B_12():

    def a_plus(self):
        msg="天可崩\n地可裂"

        with open("這是我創建的文件.txt","a+",encoding="UTF-8") as file:
            print(f"當前光標位址1:{file.tell()}")
            file.write(msg)
            print(f"當前光標位址2:{file.tell()}")
            file.seek(0)
            print(file.read())
# B_12().a_plus()
print("<<<<<")
print(">>>>>")
class C_12():
    import os
    def file_rb(self):
        with open("./歌曲素材/月光--胡彦斌.mp3","rb") as file:
            m1 = file.read()
            print(m1)
        with open("./歌曲素材/月光--胡彦斌.mp3", "wb") as file:
            print(file.write(m1))
C_12().file_rb()
print("<<<<<")
class D_12():
    import os
    def show(self):
        # 顯示當前目錄
        print(os.getcwd())
    def show2(self):
        # 顯示指定目錄下的文件夾和文件
        print(os.listdir(os.getcwd()))
        print(os.path.abspath('.'))
        print(os.path.abspath(os.path.join(os.getcwd(), os.path.pardir)))

D_12().show2()