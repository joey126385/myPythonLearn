"""
一、什么是封装？
    封装是Python、Java等面向对象语言的关键概念之一。
    像我们写讲到的 将属性（变量）和行为（方法）包装在一起作为一个类，这样的写法就是封装。
在封装中，代码和数据被包装在一个单元中，防止被意外修改。

二、什么是公有？
	在我们之前的学习中，我们封装的属性和行为都是能够公开访问的属性和行为。

三、什么是私有化？
在Python中，私有化是一种封装的概念，用于限制对类的属性和方法的访问。
私有化的目的是为了保护类的内部实现细节，防止外部代码直接访问和修改类的私有成员。

四、私有化语法？
    “变量” 或者 ”方法” 名字前面加上”单下划线” 或者 ”双下划线”即为私有。
    因此注意，在Python编程中应尽量避免使用定义以下划线开头的变量!
"""

class Phone():
    def __init__(self, brand, model):   #【 ? 】初始化手机对象
        self.brand = brand     #【 ? 】手机品牌
        self.model = model     #【 ? 】手机型号
        # 【 ? 】运行电压

    def suspend_mode(self):     #【 ? 】待机模式
        print("开启待机模式!")

    def display_info(self):     #【 ? 】查看手机详情
        print(f"品牌:{self.brand}")
        print(f"型号:{self.model}")

"""
按照需求，完善该 手机类
练习1、
    现代智能手机通常使用锂离子电池作为电源，电池的标准工作电压约为3.7伏。
当手机处于低功耗模式或待机状态时，电压可能略微降低到大约3.6伏；
而在执行高强度运算、玩游戏或其他耗能较大的任务时，电压则可能升至接近4.2伏的高点。
    需求一: 为手机类新增“运行电压私有属性”,私有属性初始值为3.7
    需求二: 当待机模式时,调整“运行电压私有属性”为3.6 

练习2、
    现代智能手机在使用中，我们通常能够查看手机的详细信息，
信息包括 手机品牌、手机型号、电池电压、以及电池状态。
    需求一: 为手机类新增检查电池状态的私有方法（电池状态自定义）,电池运行电压>3则是正常,否则电池状态为不正常
    需求二: 完善查看手机详细信息的方法，实现能在查看手机详细信息时显示电池状态。
"""









