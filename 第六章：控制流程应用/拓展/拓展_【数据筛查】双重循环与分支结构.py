"""
题目：
编写一个Python程序，给定一个包含字典的列表，每个字典代表一个商店的信息，包含"名称"、"商品列表"两个键。
其中"商品列表"也是一个列表，包含多个字典，每个字典代表一个商品，包含"名称"、"价格"和"库存"三个键。

程序需要完成以下任务：
1、遍历每个商店。
2、对于每个商店，遍历其商品列表。
3、找出所有库存大于10且价格低于50的商品，并打印出它们的名称、价格和所属商店的名称。

示例列表：
stores = [
    {
        "名称": "商店A",
        "商品列表": [
            {"名称": "商品1", "价格": 40, "库存": 5},
            {"名称": "商品2", "价格": 60, "库存": 15},
            {"名称": "商品3", "价格": 30, "库存": 20}
        ]
    },
    {
        "名称": "商店B",
        "商品列表": [
            {"名称": "商品4", "价格": 20, "库存": 8},
            {"名称": "商品5", "价格": 45, "库存": 12},
            {"名称": "商品6", "价格": 10, "库存": 30}
        ]
    }
]


预期输出：
商店商店A的商品，名称:商品3，价格: 30，库存: 20
商店商店B的商品，名称:商品5，价格: 45，库存: 12
商店商店B的商品，名称:商品6，价格: 10，库存: 30

要求：
使用嵌套循环遍历商店和商品。
对于每个商品，检查其库存和价格是否满足条件。
如果满足条件，则打印出商品的名称、价格和所属商店的名称。
"""

# 答案：

stores = [
    {
        "名称": "商店A",
        "商品列表": [
            {"名称": "商品1", "价格": 40, "库存": 5},
            {"名称": "商品2", "价格": 60, "库存": 15},
            {"名称": "商品3", "价格": 30, "库存": 20}
        ]
    },

    {
        "名称": "商店B",
        "商品列表": [
            {"名称": "商品4", "价格": 20, "库存": 8},
            {"名称": "商品5", "价格": 45, "库存": 12},
            {"名称": "商品6", "价格": 10, "库存": 30}
        ]
    }

]

for store in stores:
    store_name = store["名称"]
    for product in store["商品列表"]:
        product_name = product["名称"]
        price = product["价格"]
        stock = product["库存"]

        if stock > 10 and price < 50:
            print(f"商店{store_name}的商品，名称:{product_name}，价格: {price}，库存: {stock}")


# 运行上述代码，将输出：
# 商店商店A的商品，名称:商品3，价格: 30，库存: 20
# 商店商店B的商品，名称:商品5，价格: 45，库存: 12
# 商店商店B的商品，名称:商品6，价格: 10，库存: 30

# 解释：
# 我们首先定义了一个包含商店信息的列表stores。
# 使用外层循环遍历每个商店，获取商店的名称。
# 对于每个商店，使用内层循环遍历其商品列表。
# 在内层循环中，我们提取出商品的名称、价格和库存，并检查它们是否满足条件（库存大于10且价格低于50）。
# 如果商品满足条件，我们打印出商品的名称、价格和所属商店的名称。
# 如果商品不满足条件，则继续检查下一个商品。
# 当所有商店和商品都被检查完毕后，程序结束。