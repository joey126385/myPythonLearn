from flask import Flask,request     # 从`flask`包中导入` Flask `模块，request 用于获取请求携带参数
from flask_cors import CORS, cross_origin   # 1、导入，跨域工具
from link_mysql import link_studyFlask    # 从 link_mysql 包中 直接导入了 link_studyFlask工具

conn,cur = link_studyFlask()      # 创建数据库连接，并获取连接对象和游标
app = Flask(__name__)       # flask框架中的Flask类被用来初始化一个对象
cors = CORS(app)        # 2、用跨域工具为 flask对象修饰

# 测试接口
@app.route("/test")
def test():
    return 'Hello Flask!'

# 注册接口
@app.route('/register',methods=['POST'])
def register():
    # 获取 接口 参数
    data = request.get_json(silent=True)
    user_name = data.get('user_name')
    user_tel = data.get('user_tel')
    user_pass = data.get('user_pass')
    user_type = data.get('user_type')
    print(f"用户注册数据：{user_name}, {user_tel}, {user_pass}, {user_type}")
    # 注册业务代码
    try:
        # 创建sql
        sql = f"""
        INSERT INTO gitee_user (user_name, user_tel, user_pass, user_type)
        VALUES ('{user_name}', '{user_tel}', '{user_pass}', {user_type});
        """
        # 执行sql
        cur.execute(sql)
    except Exception as e:      # sql执行失败, 捕捉异常
        print(f"sql执行失败异常提示{e}")
        conn.rollback()
        return 'no'
    else:        # sql执行成功
        conn.commit()      # 提交事务
        return 'yes'


# 登录接口
@app.route('/login',methods=['GET'])
def login():
    # 获取 接口 参数
    user_name = request.args.get('user_name')
    user_pass = request.args.get('user_pass')
    user_tel = request.args.get('user_tel')
    # 登录业务代码
    # 创建sql
    sql = f"""
    SELECT * FROM gitee_user
    WHERE (user_name = '{user_name}' AND user_pass = '{user_pass}')
    OR (user_tel = '{user_tel}' AND user_pass = '{user_pass}');
    """
    # 执行sql,返回受影响行数
    x = cur.execute(sql)
    # 验证是否有查询到数据
    if x:
        user_msg = list(cur.fetchall())      # 由于查询到的数据是一个元组类型数据
        user_type = user_msg[0][4]     # 提取 用户类型 数据
        return str(user_type)     # 注意，这里必须转字符串类型，因为接口 返回类型必须是字符串、字典、列表、带头或状态的元组，
    else:
        return 'no'

# 测试一下 ， 确认 flask 项目是否搭建成功
if __name__ == '__main__':
    # 启动了，flask 项目
    app.run()
    # 最后关闭游标
    conn.close()
    conn.close()
