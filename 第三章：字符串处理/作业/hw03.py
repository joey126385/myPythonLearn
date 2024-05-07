"""
    A:轉義字符
"""
# 1、\n 換行符號
# 2、\t 水平製表符號(空格)
# 3、\  取消轉義
str = """
桃花坞里桃花庵，
桃花庵里桃花仙。\t
桃花仙人种桃树，\n
又摘桃花换酒钱。
酒醒只在花前坐，
酒醉还来花下眠。
"""
print(str)

"""
    B:格式化輸出
"""
# 1、+      拼接符號，用於將兩個字串拚再一起
# 2、%s     萬能佔位福，先佔著一個位置，稍後定義內容
# 3、join   拼接函数,功能是按照指定的拼接符号，拼接数据，数据必须是一个整体（一般是字符串列表或者元组）
# 4、format 格式化輸出
# 5、input()用於鍵盤接受一個用戶輸入的數據
str1 = "床前明月光"
str2 = "疑是地上霜"
resulet=str1+",\n"+str2 + "。"
print(resulet)

"""
    C:編碼規則
# 1、encode 查看編碼後的數據
    語法:str.encode(encoding="utf-8")
# 2、decode 查看解碼後的數據
    語法:str.decode(encoding="UTF-8")
"""
strC = "桃花"
x=strC.encode(encoding="utf-8")# b'\xe6\xa1\x83\xe8\x8a\xb1'
print(f"'桃花'編號後的數據是:{x}")
y=x.decode(encoding="UTF-8")
print(f"'桃花'編號後的數據是:{y}")