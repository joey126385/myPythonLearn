"""
编写一个程序，
输入一个字符串 s，
将字符串中的元音字母（a、e、i、o、u、l）
替换为大写字母并输出。
例如，
输入字符串 "hello world"，

输出 "hELLO wOrLd”。
"""
import random
import re


class  A_1():
    def a(self):
        s = input("輸入一個字串")
       # s='hello world'
        l=['a','e','i','o','u','l']
        for i in l:
            if(s.find(i)!=-1):
                s=s.replace(i,i.upper())
        print(s) 
#A_1().a()

"""
2、
用户输入班长口袋里的钱数，
若大于等于2000，请大家吃西餐。
若小于2000，大于等于1500，请大家吃快餐。
若小于1500，大于等于1000，请大家喝饮料。
若小于1000，大于等于500，请大家吃棒棒糖。
否则提醒班长下次把钱带够
"""
class B_1():
    def a(self):
        userInput=int(input("班長口袋裡的錢錢"))
        #userInput=0
        result=None
        if(500<=userInput):
            if(userInput<1000):
                result = "请大家吃棒棒糖。"
            elif (userInput<1500):
                result = "请大家喝饮料。"
            elif(userInput<2000):
                result = "请大家吃快餐。"
            else:
                result = "请大家吃西餐。"
        else:#否则提醒班长下次把钱带够
            result="下次把钱带够"
        print(result)
#B_1().a()

"""
3、
从键盘接收一个十一位的数字，
判断其是否为尾号 5 连
（最后5个数一样）的手机号。
规则：第 1 位是 1，
第二位可以是数字 358 其中之一，
后面 4 位任意数字，
最后 5   位为任意相同的数字
。例如：18601088888、13912366666 则满足。 
"""
class C_1():
    def a(self):
        s="12601088888"
        result="不滿足條件"
        # 條件 第一位是 1
        if(s.isdigit() and len(re.findall("1\d{10}", s))==1):
            list=['3','5','8']
            if((s[1] in list) and len(set(s[6:11]))==1):
               result="滿足條件"
        print(result)
C_1().a()
"""
4.创建一个人类（human），要求如下： 
    2个属性：身高（height），单位m；体重（weight），单位kg
    1个方法：BMI() 用于判断一个人的体重是否健康
     计算公式为：体重除以身高的平方，得到的结果即为bmi指数
判断依据为：
过轻：低于18.5；
正常：18.5-23.9；
过重：24-27.9；
肥胖：28-32；
非常肥胖, 高于32
   BMI的计算示例：身高为1.8m，体重为75kg，计算后bmi指数为23.1481，正常
"""
class D_human():
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight

    def bmi(self):# 计算公式为：体重除以身高的平方，得到的结果即为bmi指数
        result=None
        s=self.weight/pow(self.height,2) #float
        print(s)
        if(s>18.5):
            if(s<=23.9):
                result = "正常"
            elif(s<=27.9):
                result = "过重"
            elif(s<=32):
                result = "肥胖"
            else:
                result = "非常肥胖"
        else:
            result="过轻"
        print(result)
#D_human(1.8,75).bmi()




"""
实现输入一个字符串，
分别
统计大写字母、
小写字母、
数字、
其他字符的个数 (提示：isdigit、isupper、islower)
"""
class E_1():
    def run(self):
        # s=input()
        isdigitCount,isupperCount,islowerCount,otherCount=0,0,0,0
        userInput="aaAA222CC$dddf___"
        for i in userInput:
            if(i.isdigit()):
                isdigitCount+=1
            elif(i.isupper()):
                isupperCount+=1
            elif(i.islower()):
                islowerCount+=1
            else:
                otherCount+=1
        print(f"大写字母\t{isupperCount}\n小写字母\t{islowerCount}\n数字\t{isdigitCount}\n其他字符的个数\t{otherCount} ")
#E_1().run()


"""
划拳是古老中国酒文化的一个有趣的组成部分。酒桌上两人划拳的方法为：
每人口中喊出一个数字，同时用手比划出一个数字。
如果谁比划出的数字正好等于两人喊出的数字之和，谁就赢了，输家罚一杯酒。两人同赢或两人同输则继续下一轮，直到唯一的赢家出现。

下面给出甲、乙两人的划拳记录，请你统计他们最后分别喝了多少杯酒。

【输入】
输入第一行先给出一个正整数 N（≤100），随后 N 行，每行给出一轮划拳的记录，格式为：

甲喊 甲划 乙喊 乙划
其中喊是喊出的数字，划是划出的数字，均为不超过 100 的正整数（两只手一起划）。

【输出】
在一行中先后输出甲、乙两人喝酒的杯数，其间以一个空格分隔。

测试样例：

输入样例（ 分别是 甲喊 甲划 乙喊 乙划 ）：
5
8 10 9 12
5 10 5 10
3 8 5 12         甲赢了  乙输了   乙喝酒1
12 18 1 13       甲输了  乙赢了   甲喝酒1      
4 16 12 15        甲赢了  乙输了   乙喝酒1+1

"""
class G_1():
    import random
    def a(self):
        a=5
        numM=10
        _甲酒,_乙酒=0,0
        while a>0:
            甲喊,甲划,乙喊,乙划=random.randrange(numM),random.randrange(numM),random.randrange(numM),random.randrange(numM)
            # print(f"{甲喊}\t{甲划}\t{乙喊}\t{乙划}")
            result = f"{甲喊} {甲划} {乙喊} {乙划} "
            call=甲喊+乙喊
            if(甲喊 !=乙喊):
                if(甲划==call):
                    _乙酒+=1
                    result+=f"甲赢了  乙输了   乙喝酒{_乙酒}杯"
                elif(乙划==call):
                    _甲酒 += 1
                    result += f"甲输了  乙赢了   甲喝酒{_甲酒}杯"
            print(result)
            print(f"甲喝酒杯數{_甲酒}\t 乙喝酒杯數{_乙酒}")
            a-=1
#G_1().a()