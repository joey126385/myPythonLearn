# 公共的数据库连接工具包

# 导入 pymysql , 这是一个Python用于连接和操作MySQL数据库的库。
import pymysql

def link_studyFlask():
    """
    用于连接  study_flask 库的代码
    :return: 数据库连接对象,游标
    """
    # 写配置参数 - 字典格式 {键:值,键:值,...}
    db_config = {
        'host': '127.0.0.1',  # 127.0.0.1 代表当前本机 ip 地址
        'port': 3306,  # 3306 是，mysql 端口号
        'user': 'root',  # root 在项目里面是不能直接用的
        'password': 'rootroot',
        'db': 'dba',
        'charset': 'utf8'
    }
    # .connect() 是  pymysql 提供的用于创建连接的函数
    # 解包，将 字典中的 键值对，每个提取出来作为参数传递 ， 语法： **需要解包数据
    conn = pymysql.connect(**db_config)     # 连接成功后得到的是一个数据库连接对象
    cur = conn.cursor()       # 获取游标对象，用于对数据库中的数据进行操作工具
    return conn,cur      # 返回的元组数据