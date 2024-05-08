"""
A:集合
    一、創建集合
        語法:變數={值1,值2,值3}
    二、集合特性
        1.唯一性
        2.無序姓
        3.確定性
    三、集合運算
        1.&
        2.|
        3.-
    四、集合操作方法
        1. .add(元素)
        2. .pop()
        3. .remove(元素)
        4. .update(序列類型)
        5. 集合1.isdisjoint(集合2)
B:字典
    一、創建字典
    二、字典的特點
    三、字典的操作方法
        1. 增: .setdefault(Key,Value)
        2. 删: .clear()
        3. 删: .pop(键)
        4. 刪: .popitem()
        5. 改: oldDict.update(NewDict)
        6. 查: .get(键)
        7. 查: .keys()
        8. 查: .values()
        9. 查: .items()
"""
d1={}#　創建空字典
print(type(d1))
d2={
    #key : value
    "帳號":"Joey",
    "密碼":33,
    "帳號":"Joeysss",
    "密碼":33222
}
print(d2)
print(list(d2))
#　看KEY是否存在 沒有就新增　有的變成查詢
a=d2.setdefault("城市","台中") # 新增
a=d2.setdefault("帳號","台北") # 查詢
print(d2)
print(a)
# print(d2.clear())      # 清空
# print(d2.pop("城市"))  # 刪除 KEY
# print(d2.popitem())    # 移除最後的一筆
d3={"姓名":"林里","年龄":8,"城市":"广州"}
d2.update(d3)            #兩個 字典合併
print(d2.get("年龄"))
print(d2.keys())
print(d2.values())
print(d2.items())
"""
    作業
"""
d11={
    "名稱":"商品A",
    "價格":80,
    "數量":2
}
d22={
    "姓名":"小明",
    "年齡":22,
    "成績":90
}
l1=["商品1","商品2","商品3","商品4"]
l2=["學生1","學生2","學生3","學生4"]

p1={
    "名稱":"商品A",
    "價格":80,
    "數量":2
}
p2={
    "名稱":"商品B",
    "價格":120,
    "數量":1
}
p3={
    "名稱":"商品C",
    "價格":50,
    "數量":3
}
p4={
    "名稱":"商品D",
    "價格":150,
    "數量":1
}
product=[]
product.append(p1)
product.append(p2)
product.append(p3)
product.append(p4)
print(product)
s1={
    "姓名":"小明",
    "年齡":22,
    "成績":90
}
s2={
    "姓名":"小洪",
    "年齡":19,
    "成績":85
}
s3={
    "姓名":"小剛",
    "年齡":23,
    "成績":85
}
s4={
    "姓名":"小麗",
    "年齡":21,
    "成績":88
}
student=[]
student.append(s1)
student.append(s2)
student.append(s3)
student.append(s4)
print(student)
