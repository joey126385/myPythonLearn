"""
描述： 使用`pymysql`模块连接到MySQL数据库，并执行一些基本的数据操作
    首先, 导入了`pymysql`模块后，这是一个Python用于连接和操作MySQL数据库的库。
安裝
    `pip install pymysql`
    直接用pip安装默认是从国外仓库下载包，如果报错，可以选择换源（换中国镜像）
    换源语法： `pip install pymysql -i 镜像源`
    清华镜像源：https://pypi.tuna.tsinghua.edu.cn/simple
    阿里云：https://mirrors.aliyun.com/pypi/simple/
    实操举例： `pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple`

Python代码：
    接下来，定义一个数据库配置字典`db_config`，其中包含了连接MySQL数据库所需的信息，
    包括主机名、端口号、用户名、密码、数据库名和字符集等。
解析：
    主机名（host）【str】: 127.0.0.1，表示本地主机。(主机名 - ip : 指的是计算机的唯一标识符号)
    端口号（port）【int】: MySQL数据库的默认端口号3306。 (端口号： 程序运行后占用的数据通道)
    用户名（user）【str】:         (连接数据库时使用的用户名。)
    密码（password）【str】:       (连接数据库时使用的密码。)
    数据库名（db）【str】:           (连接到的数据库的名称。)
    字符集（charset）【str】:   utf8    (与数据库通信时使用的字符集。)
"""
# 如何用python链接上MySQL

# 一、导入 pymysql
import pymysql

# 二、定义一个数据库配置字典`db_config`，其中包含了连接MySQL数据库所需的信息
# 主机名、端口号、用户名、密码、数据库名和字符集等
db_config = {
    'host' : '127.0.0.1',
    'port' : 3306 ,
    'user' : 'buyu',
    'password' : '1024',
    'db' : 'test_b',
    'charset' :'utf8'
}

# 三、用到以上的配置信息，进行数据库连接
# **db_config : 对配置信息字典，进行解包操作，将配置信息拆解为参数去进行函数的调用
conn = pymysql.connect(**db_config)     # 创建跟数据库的链接，并获取来链接对象
cur = conn.cursor()     # 获取操作数据库数据的游标对象
# 测试
print(conn)
print(cur)

# 四、对数据库中的表格数据进行增删改查操作

# 1、导入模块后，可以去调用模块函数获取链接对象，和游标对象，这个游标对象能够操作数据库中的数据
# 2、写一条sql
# 3、通过游标对象执行这个条sql，执行完sql后，如果没有报错的话，执行结果会保存到游标对象中
# 4、通过游标对象的方法去获取sql执行结果。



# 通过Python代码查询这个Users表格（通过Python去执行sql语句）
# execute()方法用于执行sql语句，该方法会返回被影响的条数（根据sql变化的，当执行查询sql的时候，返回的被查询反行数）
# fetchall()方法用于获取所有的查询结果
# 声明了一个查询表格的函数，然后将查询表格名字提取为参数。
"""
# 1.0版本查询函数
def select_table(table_name):
    sql = f'select * from {table_name};'
    x = cur.execute(sql)
    # print(x)      # 打印查询结果条数,用于验证给程序员看sql执行是否成功
    # print(cur.fetchall())       # 打印查询结果,用于验证给程序员看sql执行是否成功
    return cur.fetchall()
"""
# 2.0版本查询函数
def select_table(table_name):
    try:
        sql = f'select * from {table_name};'
        cur.execute(sql)
    except Exception as e:
        print(f"查询失败，报错信息{e}")     # 是写给程序员看的测试代码
        return "查询失败"          # 是项目中需用用到的一个返回值
    else:
        print("查询成功")
        return cur.fetchall()    # 执行成功之后才会执行

# x = select_table("chinese")    # 在调用封装好的，执行sql的函数时，我们其实可以预知错误，这个时候可以用到异常捕捉
# print(x)

# 在做项目过程当做，一条sql不会只执行一次，会尽可能的多次利用。所以一般讲sql及其相关联的可以重复利用的代码进行封装为函数。

# 新增Users表普通用户信息
def inser_Users_notRoot(username,password):
    try:
        sql = f"insert into Users(username,password) values('{username}','{password}');"
        x = cur.execute(sql)
        print(f"新增数据条数：{x}")
    except Exception as e:
        print(f"新增失败，报错信息{e}")  # 是写给程序员看的测试代码
        conn.rollback()
        return "新增失败"
    else:
        print("新增成功！")
        conn.commit()
        return "新增成功！"

# inser_Users_notRoot("童谣",'qwe123')
# 当我们执行需要对数据库信息进行更新操作的sql时，为了数据库的一致性和可靠性，保证数据的完整性。我们需要手动的确认一下事务状态。
# 确认失败(事务回滚) : 数据库链接对象.rollback()
# 确认成功(事务提交) : 数据库链接对象.commit()

# 修改(根据用户id修改用户名和用户密码)
def update_Users_by_user_id(username,password,user_id):
    try:
        sql = f"update Users set username='{username}',password='{password}' where user_id={user_id};"
        x = cur.execute(sql)
        print(f"修改数据条数：{x}")
    except Exception as e:
        print(f"修改失败，报错信息{e}")  # 是写给程序员看的测试代码
        conn.rollback()
        return '修改失败'
    else:
        print("修改成功！")
        conn.commit()
        return '修改成功！'
# update_Users_by_user_id("麒麟","4567",5)

# 删除（课后作业）




"""
# 查询多个表格 （在项目中一般很少这样做）
li = ["chinese","courses","orders"]
for i in li:
    select_table(i)
"""


# 在程序运行完之后，记得关闭一下游标和数据库链接，防止占用太多资源
cur.close()  # 关闭游标
conn.close()  # 关闭链接
