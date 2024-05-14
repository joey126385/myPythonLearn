"""
一、擴展題目
需求1：
如果验证码校验成功，则在控制台输出"验证码正确，即将登录！"，
如果验证码校验不对，则在控制台输出"验证码错误，请重新输入！"

需求2：
在需求1实现的基础上，叠加循环，实现 
给用户三次输入错误的机会，如果三次机会用完都没有输入正确，则
提示"机器已锁死，请明日再试！"
"""
import random
yanZhenma=random.randint(1,10);
count=0; #  計算次數 從0開始
while(count<3):# 限制三次
    user_input = int(input("请填入正确的验证码："));
    if(yanZhenma==user_input):       
        break;
    print(f"验证码错误，请重新输入！{yanZhenma}");
    count+=1;5
if(count==3):
    print("机器已锁死，请明日再试！");
else:
    print("验证码正确，即将登录！");

"""
二、查酒駕
一、题目描述：
    每100毫升血液酒精含量小于20为正常驾驶， 
    大于等于20小于80为饮酒驾车， 
    大于等于80 小于100为醉酒驾驶，
    大于100以上则重新测试。
    请编辑一个程序实现这个判断功能。
二、请用循环，实现打印1-10中的所有能够被5整除的数字
三、请用循环，实现打印1-10中的所有能够被2整除的数字
四、请用循环，实现打印10-1中的所有数字
"""
driver=int(input("駕駛酒精能度"))
if(driver<20):
    print("正常驾驶");
elif(driver>=20 and driver<80):
    print("饮酒驾车");
elif(driver>=80 and driver<100):
    print("醉酒驾驶");
else:
    print("重新测试");

for i in range(10,0,-1):
    if(i%5==0):
        print(f"被5整除的數字{i}");2
    if(i%2==0):
        print(f"被2整除的數字{i}");
    print(f"所有数字{i}");
"""
商場促銷
    購物不超過200  每有折扣
    200 不超過500 九折
    超過 500 8折
"""

buy_in=int(input("輸入購買的金額"));
result=0;
if(buy_in<200):
    result=buy_in;
elif(buy_in<=200 and buy_in<500):
    result=buy_in*0.9;
else:
    result=buy_in*0.8;
print(f"購買後的金額{result}")