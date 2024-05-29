"""
todo    字串  string ''  ""  """ """  ''' '''
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
todo    列表  list()  or  []
    一、類型:可變數據類型
    二、定義:
    三、語法:[元素1,元素2,元素3,...]

todo    元組  tuple() or  ()
    一、類型:不可變數據類型
    二、定義:
    三、語法:(元素1,元素2,元素3,...)

todo    字典  dict()  or  {key1:Value ,Key2:Value2}
    一、類型:散列類型 ->沒有順序的一列數據數據


todo    集合  set()   or  {值1,值2}

todo    函數

todo    算法

"""

"""
todo    初識函數
        ?A:     函數語法
                        一、def 關鍵字 和 函數名 是必需要有的
                        二、函數名字，及函數標示符，需要符合標示符命名規則
                        三、參數列表 和 return 返回值 可以有或者可以沒有
                        四、函數語法結構->

                                def 函數名(參數列表):
                                        函數代碼
                                        return 值

                        五、函數語法調用: 函數名(參數)
                        六、【先定義函式，再執行函式】
                        七、如何使用
                                1、函數創建之後，必須通過含署名去進行調用
                                2、函數在使用的時候，是否要傳入參數，以及是否要接受返回值，是根據函數設定來的。

        ?B:     函數不同的寫法
                        一、有參數有返回值函數
                        二、有參數無返回值函數
                        三、無參數有返回值函數
                        四、無參數無返回值函數
        ?C:     函數的參數解說
                        一、必要參數
                        二、預設函數
                        三、不定長參數
                        四、關鍵字不定長參數                        
"""
"""
todo    函數作用域及匿名函數
"""

"""
todo    類和對象

"""

"""
todo    封裝和繼承

"""

"""
todo    魔法方法與裝飾器

"""

"""
todo    文件操作


"""

"""
todo    異常

"""

"""
todo    正則表達式

"""