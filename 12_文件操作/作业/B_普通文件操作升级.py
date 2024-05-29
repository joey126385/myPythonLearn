"""
什么是上下文管理？
在Python中，上下文管理器是一种用于管理资源（例如文件或网络连接）的机制，它能够确保这些资源在不再需要时被正确地释放或关闭。
通常情况下，上下文管理器被使用在with语句中，这样在进入和退出代码块时，就会自动地执行相关的操作。

上下文管理文件读写语法：
with open(文件,文件打开模式,编码格式)as 变量名:
    变量名.文件操作

filename 是文件的路径和名称，
mode 是文件的打开模式，
file 是文件对象

"""
