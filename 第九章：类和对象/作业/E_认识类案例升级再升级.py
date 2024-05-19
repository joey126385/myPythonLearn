# 制作一个小的数据采集程序

# 0、基于认识类的升级案例
# 1、通过控制台录入部分学生信息，其中学员id是程序自动生成
# 2、将录入的信息储存在对象中
# 3、将对象储存在一个序列中【该对象够存储多个学生对象，并且每个对象会存储学生对应的信息】
# 4、实现在录入且存储完一个学员信息之后，询问是否继续录入



# 类是一个模版，如果用生活中的事务理解类似于设计图纸或者表格
class Students():     # 声明一个类
    # 属性-变量：学号、姓名、年龄。。。
    def __init__(self,stuID,name,age):
        self.stuID = stuID
        self.name = name
        self.age = age

    # 行为-函数(方法)：自我介绍、学习、睡觉、吃饭、打卡。。。
    def sayHello(self):
        print("hello")
    def sayHello_plus(self):
        # 这个self代表当前类本身，这个是一个固定的写法，self在该方法进行调用的时候是不用手动传参
        # self是干嘛用的？  self代表当前类本身，里面包含了当前类已经有的属性和行为，可以通过self去调用当前类的属性和行为
        print(f"大家好，我是{self.name},我今年{self.age}岁了")

li = []   # 创建一个列表，用于储存学生对象

# 实现id是程序自动生成
ID = 0   # 用于生成学员ID，初始ID是0
while True:    # 用于实现一直循环
    # 1、通过控制台录入学生信息
    ID = ID+1   # 当录入一个学生信息，ID就+1，用于替换之前的用户输入ID
    input_name = input("请输入学生姓名：")
    input_age = int(input("请输入学生年龄："))

    # 2、将录入的信息储存在对象
    stu1 = Students(ID,input_name,input_age) # 创建一个学生对象

    # 测试输入的信息，和存储的用户数据是否一致
    print(f"用户输入：{ID}，{input_name}，{input_age}")
    print(f"系统存储：{stu1.stuID}，{stu1.name}，{stu1.age}")

    # 3、将对象储存在一个序列中，实现能够存储多个学生对象，并且可以存储每个学生对应的每个信息
    li.append(stu1)    # 将对象添加到列表中
    # print(li)   # 对象直接打印的话是不会展示具体内容的，只会展示这个对象的存储地址，就像函数直接打印也是打印一个地址
    print(len(li))    # 查看一下li的长度

    # 实现在录入一个学员信息之后，询问是否继续录入
    x = input("扣1继续，其他按键结束录入！")
    if x != "1":      # 如果用户输入的不是 1 那么结束循环
        break

print("以下为录入的学生信息：")
# 查看采集的学员信息
for student in li:
    print(f"学生id{student.stuID},姓名:{student.name},年龄:{student.age}")

