
# 什么是转义字符？
# 在Python中\加一些英文字符具有特殊的意义
# 比如字母 n 本来非常普通，加上 \ 后意义就发生了改变， \n 是换行符号

# \n 换行符号
str1 = "桃花坞里桃花庵，桃花庵里桃花仙。桃花仙人种桃树，又摘桃花换酒钱。酒醒只在花前坐，酒醉还来花下眠。"
print(str1)

str2 = "桃花坞里桃花庵，桃花庵里桃花仙。\n桃花仙人种桃树，又摘桃花换酒钱。\n酒醒只在花前坐，酒醉还来花下眠。"
print(str2)

print("----------------------------------分割线-------------------------------------")

# \t 水平制表符(空格)
# 拓展细节： \t有自己的空格规则，空格数量根据规则来定
# 当前方字符数量 <4 的时候，补齐的空格数量为 4-方字符数量
x = "abc\t123"
print(x)
# 当前方字符数量 >=4 的时候，补齐的空格数量为 8-方字符数量
y = 'abcd\t1234'
print(y)
z = 'abcdefghij\t123'
#       1   2
print(z)
# 英文字母和数字都是占1个字符，中文会根据编码规则的不同，有变化，比如有些占2个，有些占3个
str6 = "桃花坞里桃花庵，桃花庵里桃花仙。"
print(str6)

str7 = "桃花坞里桃花庵，\t桃花庵里桃花仙。"
print(str7)





# \ 取消转义
# 取消转义在地址里面用到的很多
url = 'D:\\pythonWork\\pythonBasics'    # \+字母或者字符会出现转义
# 大部分情况下，我们直接复制地址，是单斜杠的，但是由于，Python中规定 \ + 一些字符会具有特殊的意义，所以这就导致很多时候，单斜杠的地址
# 在程序中，可能会被程序误解成别的意思，导致地址失效，为了解决这个文件，我们可以采取在地址中的斜杠前面再加一个，实现取消转义。
str8 = "桃花坞里桃花庵，桃花庵里桃花仙。\\n桃花仙人种桃树，又摘桃花换酒钱。\\n酒醒只在花前坐，酒醉还来花下眠。"
print(str8)

# 想让这个打印语句不换行
print("床前明月光，",end='----')    # print语句默认是在输入完后自动换行，这个功能是如何实现？ 因为在源码中，打印一个字符后会自动加一个\n
print("疑是地上霜。")
print("疑是地上霜。")
# 在print语句中，添加一个end参数，并给这个end一个值，实际上是在覆盖print语句中end的值

# 查看源码： 将鼠标移到你要查看的代码上方，按下ctrl键，等鼠标光标变成一个小手后，点击代码。