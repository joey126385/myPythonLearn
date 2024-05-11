
# Python 不仅支持 if 语句相互嵌套，while 和 for 循环结构也支持嵌套。
# 所谓嵌套（Nest），就是一条语句里面还有另一条语句，例如 for 里面还有 for，while 里面还有 while，
# 甚至 while 中有 for 或者 for 中有 while 也都是允许的。

# 当 2 个（甚至多个）循环结构相互嵌套时，位于外层的循环结构常简称为外层循环或外循环，
# 位于内层的循环结构常简称为内层循环或内循环。


"""
题目：
编写一个Python程序，给定一个包含字典的列表，每个字典代表一个学生的信息，包含"姓名"、"年龄"和"成绩"三个键。
使用for循环遍历这个列表，将它们打印出来。

示例列表：
students = [
    {"姓名": "小明", "年龄": 22, "成绩": 90},
    {"姓名": "小红", "年龄": 19, "成绩": 85},
    {"姓名": "小刚", "年龄": 23, "成绩": 92},
    {"姓名": "小丽", "年龄": 21, "成绩": 88}
]

预期输出：
姓名:小明    年龄:22    成绩:90
姓名:小红    年龄:19    成绩:85
姓名:小刚    年龄:23    成绩:92
姓名:小丽    年龄:21    成绩:88

要求：
使用for循环遍历列表中的每个字典。

"""

students = [
    {"姓名": "小明", "年龄": 22, "成绩": 90},
    {"姓名": "小红", "年龄": 19, "成绩": 85},
    {"姓名": "小刚", "年龄": 23, "成绩": 92},
    {"姓名": "小丽", "年龄": 21, "成绩": 88}
]

for s in students:    # 让变量 s 重复从 students列表中去拿一个元素
    # print(s.items())    # 每循环一次 变量 s 都会得到一个字典
    for j in s.items():
        print(j[0],j[1],end="    ")
        # 由于当我们使用了 不换行功能， 那最后一次内循环结束的时候，它还是保留了这个不换行功能，以至于下一次循环会接着上一次不换行的地方打印
    print()   # 为了结束不换行功能

# 在嵌套循环的过程中，外循环执行一次，里面的循环要全部执行完
print("--------------------------------------------------------------")

for u in students:
    for p in u.items():
        print(p[0],p[1],end="    ")
    print()


print("--------------------------------------------------------------")
# 需要用到字典的查询方法
# 得到字典中的所有的键和值

x = [('姓名', '小明'), ('年龄', 22), ('成绩', 90)]
for i in x:   # 每循环一次变量i会取到一个元组
    print(i[0],i[1])

print("--------------------------------------------------------------")

for i in students:
    n = i["姓名"]
    a = i["年龄"]
    s = i["成绩"]
    print("姓名",n,"    年龄",a,"    成绩",s)


# 1、当只实现一样效果的时候，其实代码有很多种写法
# 2、我们程序员需要根据使用场景去抉择用哪种实现方式，当前目前初学者可能很难达到熟练的抉择，
#    这就需要大家多努力，多写多敲，必须得具备一定的编码量才能具备相应的经验

