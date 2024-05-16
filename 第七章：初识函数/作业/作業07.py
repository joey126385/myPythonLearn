"""
todo 初識函數
?[A]:  函數語法
        一、def 關鍵字 和 函數名 是必需要有的
        二、函數名字，及函數標示符，需要符合標示符命名規則
        三、參數列表 和 return 返回值 可以有或者可以沒有
        四、函數語法結構->
                def 函數名(參數列表):
                    函數代碼
                    return 值
        五、函數語法調用: 函數名(參數)
        六、【先定義函式，再執行函式】
        七、如何使用
            1、函數創建之後，必須通過含署名去進行調用
            2、函數在使用的時候，是否要傳入參數，以及是否要接受返回值，是根據函數設定來的
                          
?[B]:  函數不同的寫法
        一、有參數有返回值函數
        二、有參數無返回值函數
        三、無參數有返回值函數
        四、無參數無返回值函數
?[C]:  函數的參數解說
        一、必要參數
        二、預設函數
        三、不定長參數
        四、關鍵字不定長參數
?[D]:  其他頁面遊戲調用案例
"""
#       ! [A]:  函數語法
def show(message):  # 定義函數
    print(f"無參數內容not {message}");
    return message+'birthday';
# show("Happy");    # 調用函數
print(f"有參數的訊息{show('Happy')}");

#       ![B]:  函數不同的寫法
#       一、有參數有返回值函數
print("-----------------------------------------------------")
def b(x,y):
    return x+y;
print(b(2,3));
#       二、有參數無返回值函數
def a(x,y):
    print(x+y);
a(2,3);
#       三、無參數有返回值函數
def c():
    import random;
    x=random.choice(["1","2","3","4"]);
    return x;
c();
print(c());
#       四、無參數無返回值函數
def d():
    q=input("問題");
    ans=q.strip("s");
    print(f"問題{ans}");
#d();

#       ![C]:  函數的參數解說
#       一、必要參數
def student(weigth,heigth):
    print(f"學生身高{weigth} 體重{heigth}");
student(170,70);
#       二、預設函數
def login(login_user,le='普通'):
    print(f"登入帳號{login_user}\t 權限{le}");
login("andy");# 使用預設
login("andy","高級");

#       三、不定長參數
def test(a,b,c="預設值",*args):
    print(f"必要參數{a}{b}");
    print(f"有預設參數{c}");
    print(f"可變參數{args}");
test("aa","bb","cc","zz","xx");
#       四、關鍵字不定長參數
def test1(a,b,c="預設值",*args,**kwargs):
    print(f"必要參數{a}{b}");
    print(f"有預設參數{c}");
    print(f"可變參數{args}");
    print(f"關鍵字可變參數{kwargs}");

test1("aaa","bbb","ccc","zzz","xxx",url="www.baidu.com",path="d://pythonWork");

"""
todo python 內置函數
min(iter)
max(iter)
sum(iter)

enumerate()

ecal()  可以回傳計算的結果
exec()  無回傳解果

list()
str()
int ()
set()
"""
print("-----------------");
num=[1,2,3,4,5,6,7,8];
print(f"最小值{min(num)}");
print(f"最大值{max(num)}");
print(f"總和{sum(num)}");
print(f"總和{sum(num)}");
eval('print("hello")');
print(eval('x+y',{'x':1,'y':2}));
