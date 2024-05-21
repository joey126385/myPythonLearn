"""
A:字串  string ''  ""  """ """  ''' '''
    一、取得字元與字串
        1.[:]           :取出全部字元，從開始到結束
        2.[start: ]     :取出從start 的位置一直到結束的字元
        3.[:end]        :取出從開始一直到end的「前一個位置」字元
        4.[start:end]   :取出從start位置到end的「前一個位置」字元
        5.[start:end:step]:取出從start位置到end 的「前一個位置」字元 並跳過 step 個字元。

 !       說明範例:
                a = '0123456789abcdef'
                print(a[:])       # 0123456789abcdef ( 取出全部字元 )
                print(a[5:])      # 56789abcdef ( 從 5 開始到結束 )
                print(a[:5])      # 01234 ( 從 0 開始到第 4 個 ( 5-1 ) )
                print(a[5:10])    # 56789 ( 從 5 開始到第 9 個 ( 10-1 ) )
                print(a[5:-3])    # 56789abc ( 從 5 開始到倒數第 4 個 ( -3-1 ) )
                print(a[5:10:2])  # 579 ( 從 5 開始到第 9 個，中間略過 2 個 )      


                    
    二、內建函數:
    三、
        1.  +   :  
                拼接實現新增
        2. string.replace(str1,str2):
                把string 中的str1替換成str2
        3. string.upper():
                將所有字串的字母變成大寫
        4. string.lower():
                將所有字串的字母變成小寫
        5. string.capitalize():
                將首字轉成大寫
        6. string.split(str):
                將一個字串，根據指定的『分隔符號』拆分成『串列』
        7. string.startswith(str):
                檢查字串是否有str開頭，是返回True 否則返回 False
        8. string.endswith(str)
                檢查字串是否有str結束，是返回True 否則返回 False
B:列表  list()  or  []
    一、類型:可變數據類型
    二、定義:
    三、語法:[元素1,元素2,元素3,...]

C:元組  tuple() or  ()
    一、類型:不可變數據類型
    二、定義:
    三、語法:(元素1,元素2,元素3,...)

D:字典  dict()  or  {key1:Value ,Key2:Value2}
    一、類型:散列類型 ->沒有順序的一列數據數據


E:集合  set()   or  {值1,值2}

F:函數

G:算法

"""