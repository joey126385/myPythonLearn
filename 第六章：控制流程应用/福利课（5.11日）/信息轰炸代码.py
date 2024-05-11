# 消息轰炸小脚本-使用教程：打开终端

# 工具库：pynput用于通过代码去模拟人工操作键盘和鼠标，它是一个第三方工具库

# 1、win电脑，按下键盘的 win+r 键盘，在打开的运行窗口中输入cmd,即可以打开cmd窗口
# 2、 输入 pip install pynput -i https://pypi.douban.com/simple/
# 3、安装好包后，导入包，以待使用


# 从某个大的工具库中，拿到一个具体的工具
# 从 pynput 中的键盘模块中，导入键盘和键盘控制器
from pynput.keyboard import Key,Controller
# 导入时间模块
import time

# 1、发什么消息？
x = input("请输入你要发送的信息（仅限中文）：")
# 2、消息发送次数？
y = input("请输入消息发送次数：")
# 3、多少秒后发送
z = input("多少秒后发送：")

# # 准备发送消息(实现读秒功能)
# for i in range(int(z),0,-1):
#     print(f"{i}秒后发送信息！")
#     time.sleep(1)   # 用来让程序休眠的，实现程序运行暂停一小会的功能，暂停单位是秒

for i in range(int(z),0,-1):
    print("\r倒数", i, end=" 秒后进行消息轰炸...")
    time.sleep(1)

# 在读秒结束后实现用代码发送信息
kb = Controller()      # 创建一个控制键盘对象
for i in range(0,int(y),1):
    kb.type(x)  # 通过代码操控键盘模拟用户输入信息
    # 通过代码操作电脑模拟人手去按下enter键 ， 1、按下 2、松开
    kb.press(Key.enter)
    kb.release(Key.enter)

