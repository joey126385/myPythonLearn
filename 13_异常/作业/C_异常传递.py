# 异常具有传递性

# 以下为演示异常传递性的案例：
# 零除：在数学中，将一个数除以零的操作，通常被认为是未定义的，因为它没有唯一的结果。

def func01():
    print("这是func01开始")
    num = 1 / 0      # ZeroDivisionError 除数为0异常
    print("这是func01结束")

def func02():
    print("这是func02开始")
    func01()
    print("这是func02结束")

def main():
    func02()

main()





