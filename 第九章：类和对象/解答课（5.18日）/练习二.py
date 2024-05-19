"""
1、从控制台接收一个不大于1000的正整数n,
统计1-n中不能被5整除的数的个数
累加1-n中能被5整除,且能被2整除的数的和
"""

"""
# input 输入语句，用于从控制台接受一个键盘输入的数据，这个数据会自动保存为字符串数据进行返回
n = int(input("请输入一个不大于1000的正整数："))
c1,c2 = 0,0        # 同时申明两个变量,c1用于统计个数，c2用于累加
for i in range(1,n+1,1):
    if i%5!=0:    # 判断当前变量是否不能被5整除
        c1 = c1+1
    elif i%5==0 and i%2==0:     # 判断 是否 能被5整除,且能被2整除
        c2 = c2+i
# 当我们在打印的时候，可以用f修饰字符串，这样该字符串就可以是一个格式化字符串，字符串中可以通过{}直接拼接变量
print(f"不能被5整除的数的个数是：{c1}\n能被5整除,且能被2整除的数的和:{c2}")
"""


"""
2、从控制台接收一个不大于1000的正整数n,并输出以下三类数字：
A1=能被5整除的数字中所有偶数的和；  ---> 数字%5==0 and 数字%2==0
A2=被7整除后余1的数字的个数；  --->  数字%7==1
A3=被9整除,且能够被2整除的数字的个数。  --->  数字%9==0 and 数字%2==0
"""
n = int(input("请输入一个不大于1000的正整数："))
A1,A2,A3 = 0,0,0      # 一次性声明三个变量，分别用于累加，统计，统计
for k in range(1,n+1,1):
    if k%5==0 and k%2==0 :
        A1 = A1 + k
    elif k%7==1 and k!=1:      # 1被7整除余后余1
        A2 = A2 + 1
    elif k%9==0 and k%2==0 :
        A3 = A3 + 1
print(f"能被5整除的数字中所有偶数的和:{A1}\n被7整除后余1的数字的个数:{A2}\n被9整除,且能够被2整除的数字的个数:{A3}")

# 问题：有些数据既满足A1又满足A2也满足A3，这个该怎么解决？

n = int(input("请输入一个不大于1000的正整数："))
A1,A2,A3 = 0,0,0      # 一次性声明三个变量，分别用于累加，统计，统计
for k in range(1,n+1,1):
    if k%5==0 and k%2==0 :
        A1 = A1 + k
    if k%7==1 and k!=1:      # 1被7整除余后余1
        A2 = A2 + 1
    if k%9==0 and k%2==0 :
        A3 = A3 + 1
print(f"能被5整除的数字中所有偶数的和:{A1}\n被7整除后余1的数字的个数:{A2}\n被9整除,且能够被2整除的数字的个数:{A3}")


# 总结： if + elif 这样的写法下，这个判断是一个整体，只要满足 if 或 elif 其中的一个条件，其他的条件就不会再判断了，
#       某些情况下我们需要判断多次，可以使用多个if,多个if都是互相独立的。