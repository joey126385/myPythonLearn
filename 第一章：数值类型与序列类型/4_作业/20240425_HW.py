"""
    1. 根据数据识别以下数据类型（在注释符号# 后面写上数据类型）。
"""
# 10086 #    int
# 0.0 #     float
# 0 #       int
# False #   Boolean
# 1 - 2j #  complex
# (10086) # tuple
# [9527] # list
# (9527,) # tuple
# 'hello world' #str 单引号字符串
# "hi world" #str
# a = """换个
# 行""" #str
# None # 拓展：表示空类型，什么都没有 NoneType

"""
    2. 创建一个变量存储数据 5.20 并打印其类型。
"""
num=5.2;
print(type(num))
"""
    3. 以下中文对应的是什么python中的哪些单词？忘记了就去查一下（写在 -- 符号后面）
"""
# 整型 -- int
# 浮点型 --float
# 字符串 --str
# 布尔型 --bool
# 列表 -- list
# 元组 -- tuple
"""
    6. 创建一个空列表和一个空元组，使用变量存储它们。
"""
a6=[];
b6=();
print(type(a6),type(b6));

"""
    7. 创建一个只有一个元素的元组，元素随意写。
"""
a7=('a7',)
print(type(a7))
"""
    9. 思考以下打印的结果是什么？(在注释符号# 后面写执行结果)
"""
# a = 10
# print(a) # 10
# b = a
# print(b) #10
# b = 9
# print(c) # error 沒有這個變數


"""
    10.思考以下代码最终打印输出什么？(在注释符号# 后面写执行结果)
"""
# a_ = [[1,2,3,4,5]]
# print(a_[0]) #[1,2,3,4,5]
# print(a_[0][2]) #3
# print(a_[1]) # error  沒有索引
# # 注意：这题很容易出错，仔细审题哦~