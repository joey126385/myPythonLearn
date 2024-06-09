
# 使用re正则库
# 导入
import re
text = '''[
        {张三身高:178, 体重：168, 学号：123456, 密码:1024}
        {李四身高:188, 体重：138, 学号：123-456, 密码:1024}
       ]'''
# 查找所有
print(re.findall("1024", text))
print(re.match(r"\[", text).group())
print(re.search("体重", text).group())

import re

text = '''[
        {张三身高a:178, 体重c:168, 学号: , 密码:1024}
        {李四身高b:188, 体重d:138, 学号:123-456, 密码:1024}
       ]'''
# 单元字符
print(".匹配任意字符",re.findall(r"{(..)身", text))
print("\d 匹配数字",re.findall(r"\d",text))
print("\D 匹配非数字",re.findall(r"\D",text))
print("\d结合\D使用",re.findall(r"\d\d\d\D\d\d\d", text))
print("",re.findall(r"\w:\d", text))
print("",re.findall(r"[张三身高体重学号]", text))
text = "12345hello , ! $ % * ("
print(re.findall(r"\W", text))
# 数量修饰元字符
print(re.findall(r"学号.{,8}", text))
print(re.findall(r"学号:\d*", text))
print(re.findall(r"学号:\d+", text))
print(re.findall(r"学号:\d?", text))
# 组合元字符
print(re.findall(r"\d+-\d+", text))

text2 = '''[
            {姓名:张三, 电话: 18887654321, 幸运数:01234567891, 座机:0511-52152166}
            {姓名:李四, 电话: 18887654321, 幸运数:01234567891, 座机:0511-52152166}
        ]'''
# 多种情况组合字符
# \d{11}  匹配连在一起的11位数字
# \d{4}-\d{8}  匹配格式为 四位数字-八位数字
# | 或者的意思
print(re.findall(r"\d{11}|\d{4}-\d{8}", text2))
# 匹配 电话和座机
print(re.findall(r"1\d{10}|\d{4}-\d{8}", text2))

text2 = '姓名:张三, 电话: 18887654321, 幸运数:01234567891, 座机:0511-52152166'
# 边界元字符
print(re.findall(r"^张三", text2))
print(re.findall(r"66$", text2))
# 匹配 张三 两个字旁边没有汉字、字母、数字啥的，是其他的字符
print(re.findall(r"\b张三\b", text2))
# 匹配 运 字旁边 ，不是其他的字符，是汉字，字母，数字啥的。
print(re.findall(r"\B运\B", text2))

x = 'hhhh1234567'
print(re.findall(r"[1234]", x))  #匹配1234
print(re.findall(r"[^1234]", x))  #不匹配1234

text3 = '随机电话：13634567891，座机1：0571-52152166，座机2：0571-52152188-1234'
"""
1,确定模式包含几个子模式
13634567891   11位数字
0571-52152166   3~4位数字-7~8位数字
0571-52152188-1234  3~4位数字-7~8位数字-3~4位数字

2,各个部分的字符分类是什么
\d  -

3,各个子模式如何重复

13634567891   11位数字   \d{11}
0571-52152166   3~4位数字-7~8位数字     \d{3,4}-\d{7,8}
0571-52152188-1234  3~4位数字-7~8位数字-3~4位数字       \d{3,4}-\d{7,8}-\d{4}
"""
print(re.findall(r"\d{11}|\d{3,4}-\d{7,8}|\d{3,4}-\d{7,8}-\d{4}", text3))
