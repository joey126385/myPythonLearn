# min()	返回给定参数的最小值，参数可以为序列。
li1 = [1,2,3,4,5,6]
x = min(li1)
print(x)

# max()   返回给定参数的最大值，参数可以为序列。
li2 = [1,2,3,4,5,6]
y = max(li2)
print(y)

# sum()   对序列进行求和计算。
li3 = [1,2,3,4,5,6,7,8,9,10]
print(sum(li3))

# enumerate()   用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
#               同时列出数据和数据下标，返回enumerate对象实例
li4 = ["张三","李四","王","宋六"]
z = enumerate(li4)
for i in z:
    print(i)

# eval()   将字符串str当成有效的表达式来求值并返回计算结果。
str1 = "1024+1024"
print(eval(str1))

# exec()   执行以string类型存储的Python代码
str2 = "print('hello !')"
exec(str2)

# list()   用于创建一个空的列表对象或将可迭代对象（如字符串、元组、集合、字典等）转换为列表。
strs = "张三"
print(list(strs))
# str()   用于将对象转换为字符串表示形式。
li4 = ["张三","李四","王","宋六"]
a = str(li4)
print(a,type(a))
# int()   用于将对象转换为整数（即整型）
b = "1"
b = int(b)
print(b,type(b))
# set()   用于创建一个空的集合对象或将可迭代对象转换为集合。
li2 = [1,2,3,4,5,6,1,1,1]
set2 = set(li2)
print(set2,type(set2))