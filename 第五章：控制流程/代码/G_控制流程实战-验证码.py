"""
验证码案例
需求：
1、通过随机模块，得到一个随机数
2、使用input函数模拟，用户输入的功能，得到用户输入的验证码
3、进行验证码校验：
    如果验证码校验成功，则在控制台输出"验证码正确，即将登录！"，
    如果验证码校验不对，则在控制台输出"验证码错误，请重新输入！"
4、叠加循环，实现 给用户三次输入错误的机会，如果三次机会用完都没有输入正确，则提示"机器已锁死，请明日再试！"
"""
# 以下为提示代码
import random       # 导入随机工具包
yanZhenMa = random.randint(100000,999999)   #  通过随机工具包中一个名为randint的工具，获取100000 到 999999 中的一个随机数
print(yanZhenMa)      # 打印得到的随机数
x = input("请填入正确的验证码：")
y = int(x)   # 继续数据类型转换








# 以下为参考答案：
# import random
# yanZhenMa = random.randint(100000,999999)
# print(yanZhenMa)
#
# # 能够给用户三次输入机会
# n = 0
# while n<3 :
#     user_input = input("请填入正确的验证码：")
#     user_input = int(user_input)
#     if user_input==yanZhenMa:
#         print("验证码正确，即将登录！")
#         break
#     else:
#         print("验证码错误，请重新输入！")
#     n = n+1
#
# # 判断 输入次数是否 =3
# if n==3:
#     print("机器已锁死，请明日再试！")