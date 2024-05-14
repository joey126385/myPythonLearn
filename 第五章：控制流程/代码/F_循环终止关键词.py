"""
在Python中，用于循环终止的关键词主要有两个：break 和 continue。这两个关键词在循环控制中非常有用，可以帮助你根据特定条件灵活地控制循环的执行流程。

一、break：
    break 语句用于立即退出当前循环，无论是 for 循环还是 while 循环。当 break 语句被执行时，循环会立即停止，程序会继续执行循环之后的语句。

示例：
#在这个例子中，当 i 等于 5 时，break 语句会被执行，循环会立即停止，因此只会打印出 0 到 4。
for i in range(10):
    if i == 5:
        break
    print(i)


二、continue：
    continue 语句用于跳过当前循环的剩余部分，并进入下一次循环迭代。continue 之后的代码在当前循环迭代中不会被执行。

示例：
#在这个例子中，当 i 等于 5 时，continue 语句会被执行，因此不会打印出 5，而会继续执行下一次循环迭代。
for i in range(10):
    if i == 5:
        continue
    print(i)
"""
for i in range(10):
    if i == 5:
        continue
    print(i)

