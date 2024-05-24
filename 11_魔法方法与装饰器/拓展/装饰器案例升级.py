# 引入一下 时间库
import time
# add_plus就是一个装饰器，待会可以用于为 禁言1.0版本 进行功能升级，升级为 2.0
def add_plus(x):
    # 内层函数，用于实现具体的功能升级代码
    def plus():
        print("开始禁言！")
        x()
        for i in range(10,0,-1):
            print(f"\r禁言倒计时{i}秒",end="")
            time.sleep(1)     # 让程序休眠(停顿)的函数
        print("\r禁言结束~")
    return plus

# 模拟游戏禁言的函数 禁言1.0版本
@add_plus
def banned_to_post():
    print("正在禁言中")

banned_to_post()
