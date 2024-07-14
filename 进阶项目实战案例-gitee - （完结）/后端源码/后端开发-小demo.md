# 后端开发-小demo

```
目的：开发一个平台（网站）
	- 前端开发：HTML、CSS、JavaScript
	- Web框架：接收请求并处理
	- MySQL数据库：存储数据地方

快速上手：
	基于Flask Web框架让你快速搭建一个网站出来。
	
深入学习（web项目阶段会详细学习）：
	基于Django框架（主要）
```



## 一、快速搭建网站后台

#### 1、准备工作：

> 首先, 导入`flask`模块，这是一个Python用于搭建网站的Web框架包
>
> #### 安裝
>
> `pip install flask`
>
> 直接用pip安装默认是从国外仓库下载包，如果报错，可以选择换源（换中国镜像）
> 换源语法： `pip install flask -i 镜像源`
>
> 清华镜像源：https://pypi.tuna.tsinghua.edu.cn/simple
>
> 阿里云：https://mirrors.aliyun.com/pypi/simple/
>
> 实操举例： `pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple`



### 2、快速上手搭建步骤：

- #### 导入` Flask `模块

  ```Python
  from flask import Flask     # 从`flask`包中导入` Flask `模块
  ```

- #### 创建一个`Flask`对象

  ```Python
  from flask import Flask
  app = Flask(__name__)    # flask框架中的Flask类被用来初始化一个应用程序实例
  ```

- #### 创建一个 `函数 `

  ```Python
  from flask import Flask
  app = Flask(__name__)
  
  def test():        # 测试接口函数
      return "hell Flask !"
  ```

- #### 创建了`路由` 和 `函数` 之间的对应关系

  ```Python
  from flask import Flask
  app = Flask(__name__)
  
  # 使用flask对象中的route装饰器功能，
  # 以后用户在浏览器上访问 flask项目地址+ /test 路由，网站自动执行 test 接口函数
  @app.route("/test")    
  def test():
      return "hell Flask !"
  ```

- #### 启动 flask 对象

  ```Python
  from flask import Flask
  app = Flask(__name__)
  
  @app.route("/test")
  def test():
      return "hell Flask !"
  
  if __name__ == '__main__':   
      app.run()      # 启动
  ```

- #### 完整代码

  ```Python
  from flask import Flask
  app = Flask(__name__)
  
  @app.route("/test")
  def test():
      return "hell Flask !"
  
  if __name__ == '__main__':
      app.run()  
  ```



## 二、网站后台应用

### 1、浏览器直接 访问后端 接口

- #### 启动项目，找到运行控制台中的 Running on 后方的后台访问地址。

![image-20231117164628548](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231117164628548.png)

- #### 打开浏览器，将` 后台访问地址` 拼接 `路由地址`  进行访问

![image-20231117165046243](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231117165046243.png)



### 2、前端 axios 访问后端接口

------

前端代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
    <script src="./包/vue.js"></script>
    <script src="./包/axios.js"></script>
</head>
<body>
    <div id="box">
        <h1 style="color: crimson;">
            {{test_value}}
        </h1>
        <button @click="test">点我,请求test接口</button>
    </div>

    <script>
        new Vue({
            el : '#box',
            data : {
                test_value : null     // 用于接收 请求 test接口 响应的数据
            },
            methods : {
                test(){
                    axios({
                        method : 'get',
                        url : 'http://127.0.0.1:5000/test'
                    }).then((res)=>{
                        console.log(res);
                        this.test_value = res.data
                    })
                }
            }
        })
    </script>
</body>
</html>
```

***注意：直接axios访问会触发一个跨域问题***

#### 什么是跨域问题？

​	**跨域问题是指当一个网页的脚本试图向不同的域（协议、域名、端口）发起请求时所面临的安全限制。浏览器出于安全考虑，限制了页面中的 JavaScript 代码对不同域的资源进行访问。这种限制被称为同源策略（Same-Origin Policy）。**

![image-20231117170125589](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20231117170125589.png)

- #### 解决跨域问题

`flask_cors` 是 Flask 框架的一个扩展，用于处理跨源资源共享（CORS）的问题。CORS 是一种用于在浏览器和服务器之间进行跨源通信的机制，允许一个源（域、协议和端口的组合）的网页访问另一个源的资源。

**简而言之，`flask_cors` 的作用是帮助你处理跨域请求，让你的 Flask 应用能够安全地与其他源进行通信。**

#### 准备工作：

> 首先, 导入`flask_cors`模块
>
> #### 安裝
>
> `pip install flask_cors`
>
> 直接用pip安装默认是从国外仓库下载包，如果报错，可以选择换源（换中国镜像）
> 换源语法： `pip install flask_cors -i 镜像源`
>
> 清华镜像源：https://pypi.tuna.tsinghua.edu.cn/simple
>
> 阿里云：https://mirrors.aliyun.com/pypi/simple/
>
> 实操举例： `pip install flask_cors -i https://pypi.tuna.tsinghua.edu.cn/simple`

```python
# 1、导入，跨域工具
from flask_cors import CORS, cross_origin
```

```python
# 2、用跨域工具为 flask对象修饰
cors = CORS(app)
```

- #### 完整代码

  ```Python
  from flask import Flask
  from flask_cors import CORS, cross_origin	# 1、导入，跨域工具
  
  app = Flask(__name__)
  cors = CORS(app)	# 2、用跨域工具为 flask对象修饰
  
  @app.route("/test")
  def test():
      return "hell Flask !"
  
  if __name__ == '__main__':
      app.run()  
  ```



## 三、Get与Post请求处理：

在创建了`路由` 和 `函数` 之间的对应关系的时候，即配置路由的时候，`.route` 还有其他的用法。在 Flask 中，你可以使用 `.route` 来指定不同的 HTTP 请求方法，例如 GET、POST 等。例如：

```python
@app.route("/insert",methods=["get"])
def insert():
    # 新增逻辑代码
    return '新增成功！'
```

**这段代码表示当用户以 GET 方法访问 "/insert" 路径时，将会触发相应的处理逻辑。**



**我们都知道，在前端页面上的数据，想要提交到后台：**

- `axios`进行get请求。
  - 提交方式：`method : "get"`
  - 提交的地址：`url : "/xxx/xxx/xx"`
  - 参数：`params`
- `axios`进行post请求。
  - 提交方式：`method : "post"`
  - 提交的地址：`url : "/xxx/xxx/xx"`
  - 参数：`data`

**那后台接受数据方式呢？：**

### 1、在导入Flask 包的后面加上一个 request 

```python
# 导入 flask 包，以及 request 包
from flask import Flask,request
```

导入了request包后就可以获取前端提交的数据了

### 2、**`request.args `获取get， `request.get_json(silent=True)` 获取post**

#### 获取get数据

> **`data = request.args` 是在 Flask 中用于获取 GET 请求发送的查询参数的方法。当客户端通过 GET 请求发送查询参数时，可以使用 `request.args` 来获取这些参数。**
>
> **在 Flask 中，`request.args` 返回一个类似字典的对象，其中包含了客户端发送的查询参数。**
>
> **我们可以通过键名来访问相应的参数值。**

以下是一个简单的示例，演示了如何在 Flask 中使用 `request.args` 获取 GET 请求发送的查询参数：

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/example', methods=['GET'])
def example():
    name = request.args.get('name')  # 获取名为 'name' 的查询参数
    age = request.args.get('age')    # 获取名为 'age' 的查询参数
    return f'Name: {name}, Age: {age}'

if __name__ == '__main__':
    app.run()
```

**在这个示例中，`request.args` 用于获取 GET 请求发送的查询参数。可以通过 `request.args.get()` 方法来获取特定名称的查询参数的值。**



#### 获取post数据

> **`request.get_json(silent=True)` 是 Flask 中用于获取 POST 请求发送的` JSON` 数据的方法。**
>
> **参数 `silent=True` 表示如果请求的数据不是有效的` JSON` 格式，`get_json` 方法不会抛出异常，而是返回 `None`。**
>
> **这个方法通常用于处理接收到的` JSON` 数据。如果请求的数据是有效的 `JSON` 格式，`get_json` 方法会返回一个包含` JSON `数据的 Python 字典；如果请求的数据不是有效的` JSON `格式，且 `silent=True`，则会返回 `None`。**

以下是一个示例，演示了如何在 Flask 中使用 `request.get_json(silent=True)` 获取 POST 请求发送的 JSON 数据：

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/example', methods=['POST'])
def example():
    if request.method == 'POST':
        data = request.get_json(silent=True)  # 获取 JSON 数据
        return data

if __name__ == '__main__':
    app.run()
```

**在这个示例中，`request.get_json(silent=True)` 用于获取 POST 请求发送的 JSON 数据。如果请求的数据是有效的 JSON 格式，它会返回一个包含 `JSON` 数据的 Python 字典；如果请求的数据不是有效的 JSON 格式，且 `silent=True`，则会返回 None。**

**`json数据`补充：**

> `JSON`（JavaScript Object Notation）是一种轻量级的数据交换格式，它以易于阅读和编写的文本形式表示结构化数据。`JSON` 数据由键值对组成，键和值之间使用冒号分隔，不同键值对之间使用逗号分隔，整个数据被包裹在大括号 `{}` 中表示一个对象，或者方括号 `[]` 中表示一个数组。
>
> 以下是一个简单的 `JSON` 数据示例：
>
> ```json
> {
>   "name": "Alice",
>   "age": 25,
>   "isStudent": true,
>   "courses": ["Math", "Science", "History"]
> }
> ```
>
> 在这个示例中，`JSON` 数据表示了一个包含姓名、年龄、是否为学生以及所修课程的信息。其中，`name`、`age`、`isStudent` 是键，对应的值分别是 "Alice"、25、true；`courses` 是一个键，对应的值是一个包含多个字符串的数组。
>
> `JSON` 数据通常用于在不同系统之间进行数据交换，例如在 Web 应用中，前端和后端之间通过` JSON` 数据进行通信；在不同服务之间，通过 `JSON` 数据进行 `API` 调用等。 `JSON` 数据的简洁性和易读性使其成为一种流行的数据交换格式。



**后端代码举例：**

```Python
# 从`flask`包中导入` Flask `模块
from flask import Flask,request
# 1、导入，跨域工具
from flask_cors import CORS, cross_origin

from link_user import link_mysql
conn,cur=link_mysql()

# flask框架中的Flask类被用来初始化一个对象
app = Flask(__name__)
# 2、用跨域工具为 flask对象修饰
cors = CORS(app)

# 创建一个函数  --- 接口
@app.route("/test")     # 声明 一个路由 和函数之间的练习
def test():
    return 'Hello Flask!'

# 注册接口
@app.route("/register",methods=['POST','GET'])
def register():
    print(request.method)
    if request.method=='POST':
        # 获取 JSON 数据
        # data = request.json
        data = request.get_json(silent=True)
        print("-------",data)
        return data
    elif request.method=='GET':
        name = request.args.get('name')  # 获取查询参数
        age = request.args.get('age')
        return f'Name: {name}, Age: {age}'
    return 'hhh'


# 测试一下 ， 确认 flask 项目是否搭建成功
app.run()     # 启动了，flask 项目
```



# 四、后端处理数据



## 1、数据库准备工作：

#### **1.1、在数据库中建表：**

```sql
create table gitee_user (
    user_id int auto_increment primary key,
    user_name varchar(20) unique,
    user_tel char(11) unique,
    user_pass varchar(20),
    user_type int
);
```

这是一个创建名为 `gitee_user` 的表的 `SQL` 语句，其中包括了以下字段：

- user_id：【账户编码】整数类型，主键，自动增长
- user_name：【账户名称】最大长度为 20 的字符串类型 , 唯一约束
- user_tel：【账户绑定电话号码】长度为 11 的字符类型  , 唯一约束
- user_pass：【账户密码】最大长度为 20 的字符串类型
- user_type：【账户类型、（0游客、1用户、2超管）】整数类型

这个表的设计用于存储用户信息，包括用户的姓名、电话、密码、类型和状态。

可以选择插入几条测试数据，然后查询看看表格能不能用

```sql
insert into gitee_user (user_name, user_tel, user_pass, user_type) 
values ('testuser', '12345678901', 'password123', 1);
```

这条 `SQL` 语句将会在 `gitee_user` 表中插入一条测试数据，其中包括了 `user_name`、`user_tel`、`user_pass` 和 `user_type` 字段的值。在这个示例中，我们插入了一个用户名为 'testuser'，绑定电话号码为 '12345678901'，密码为 'password123'，账户类型为 1 的测试数据。

#### 1.2、创建数据库链接公共模块

#### 准备工作：

> 首先, 导入了`pymysql`模块后，这是一个Python用于连接和操作`MySQL`数据库的库。
>
> ##### 安裝
>
> `pip install pymysql`
>
> 直接用pip安装默认是从国外仓库下载包，如果报错，可以选择换源（换中国镜像）
> 换源语法： `pip install pymysql -i 镜像源`
>
> 清华镜像源：https://pypi.tuna.tsinghua.edu.cn/simple
>
> 阿里云：https://mirrors.aliyun.com/pypi/simple/
>
> 实操举例： `pip install pymysql -i https://pypi.tuna.tsinghua.edu.cn/simple`

#### Python代码：

> 接下来，定义一个数据库配置字典`db_config`，其中包含了连接MySQL数据库所需的信息，包括主机名、端口号、用户名、密码、数据库名和字符集等。
>
> ```
> 参数解析：
> 主机名（host）【str】: 127.0.0.1，表示本地主机。(主机名 - ip : 指的是计算机的唯一标识符号)
> 端口号（port）【int】: MySQL数据库的默认端口号3306，虚拟机是3307。 (端口号： 程序运行后占用的数据通道)
> 用户名（user）【str】:    buyu24       (连接数据库时使用的用户名。)
> 密码（password）【str】:   1024     (连接数据库时使用的密码。)
> 数据库名（db）【str】:    pyvip24       (连接到的数据库的名称。)
> 字符集（charset）【str】:   utf8    (与数据库通信时使用的字符集。)
> ```

```python
import pymysql
# db_config  -> 数据库配置（Database Configuration）。数据库配置是用来连接和配置数据库的信息，包括数据库的主机名、端口号、用户名、密码等。
db_config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': '你自己的mysql账号',
    'password': '你自己的账号密码',
    'db': '数据库名',
    'charset': 'utf8'
}
```

> 然后，使用`pymysql.connect()`函数根据数据库配置创建一个数据库连接对象`conn`，并使用该连接对象创建一个游标对象`cur`。
>
> 游标对象（Cursor Object）是数据库连接中的一种机制，用于在数据库结果集中进行导航和操作。它允许应用程序在结果集中逐行或批量获取数据，并对数据进行增、删、改和查询等操作

```python
# 关键字参数解包:使用 ** 时，它可以将一个字典中的键值对作为关键字参数传递给函数。
conn = pymysql.connect(**db_config)  # 获取链接对象
cur = conn.cursor()     # 游标对象
```

> ```
> # 演示一下错误连接情况
> # ValueError: port should be of type int    报错原因，端口号参数传的应该是int数据
> # pymysql.err.OperationalError: (1045, "Access denied for user 'buyu24'@'localhost' (using password: YES)")    端口号错误
> # 端口无效（虚拟机端口未转发  或者  虚拟机未开启）
> # pymysql.err.OperationalError: (2003, "Can't connect to MySQL server on '127.0.0.1' ([WinError 10061] 由于目标计算机积极拒绝，无法连接。)")
> ```

完整链接代码：

```Python
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
        'password': '123456',
        'db': 'study_flask',
        'charset': 'utf8'
    }
    # .connect() 是  pymysql 提供的用于创建连接的函数
    # 解包，将 字典中的 键值对，每个提取出来作为参数传递 ， 语法： **需要解包数据
    conn = pymysql.connect(**db_config)     # 连接成功后得到的是一个数据库连接对象
    cur = conn.cursor()       # 获取游标对象，用于对数据库中的数据进行操作工具
    return conn,cur      # 返回的元组数据
```



## 2、实现接口

根据项目分析数据表格需要字段和需要接口

**整个demo项目只需要两个接口，一个登录接口，一个注册接口。**

### 2.1、登录接口分析：  

```python
接口需求：
​		1、根据用户输入的 账号、密码  or 手机号、密码 去数据库进行账号验证
​		2、若用户存在，则返回当前账号类型。
接口参数： 
​		参数1：账号/电话号码 
​		参数2：密码
返回结果：
​		验证成功：返回当前账号类型
​		验证失败：返回字符串" no "
```

**可以使用以下 `SQL` 语句来实现根据账号密码登录或者电话号码和密码登录的验证：**

```sql
SELECT * FROM gitee_user 
WHERE (user_name = '输入的账号' AND user_pass = '输入的密码')
OR (user_tel = '输入的电话号码' AND user_pass = '输入的密码');
```

在这个 `SQL` 语句中，我们使用了 `SELECT` 语句来从 `gitee_user` 表中选择数据。通过使用 `WHERE` 子句，我们可以指定多个条件来进行查询，以实现根据账号密码登录或者电话号码和密码登录的验证。

**由于我们需要验证成功后获取当前账号类型并返回，所以我们可以在做完登录验证之后像这样，获取一下 “用户类型” 数据：**

> **注意 ！！！：以下代码是登录验证的示例代码，不是完整接口代码**
>
> ```python
> # 调用数据库连接工具，创建数据库连接，并获取连接对象和游标
> conn,cur = link_studyFlask()
> # 创建sql
> sql = """
> SELECT * FROM gitee_user 
> WHERE (user_name = '输入的账号' AND user_pass = '输入的密码')
> OR (user_tel = '输入的电话号码' AND user_pass = '输入的密码');
> """
> # 执行sql,返回受影响行数
> x = cur.execute(sql)
> # 验证是否有查询到数据
> if x:
>     user_msg = list(cur.fetchall())      # 由于查询到的数据是一个元组类型数据
>     user_type = user_msg[0][4]     # 提取 用户类型 数据
>     print(user_type)
> else:
>     print("当前用户不存在")
> ```

### 2.2、注册接口分析：  

```python
接口需求：
​		1、将用户输入的 账户昵称、账号类型、手机号码、账号密码 存入数据库，新增为一条数据
​		2、新增成功，返回yes,新增失败返回no
接口参数： 
​		参数1：账户昵称
​		参数2：账号类型
​		参数3：手机号码
​		参数4：账号密码
返回结果：
​		验证成功：返回字符串" yes "
​		验证失败：返回字符串" no "
```

**假设用户进行了注册操作，例如：**

- 用户名: "john_doe"
- 电话号码: "12345678900"
- 密码: "securepass"
- 用户类型: 2

那么对应的 `SQL` 语句将会是：

```sql
INSERT INTO gitee_user (user_name, user_tel, user_pass, user_type) 
VALUES ('john_doe', '12345678900', 'securepass', 2);
```

这条` SQL` 语句将会向 `gitee_user` 表中插入一条新的数据，其中包括了用户名、电话号码、密码和用户类型的值。

**由于，当python链接数据库的时候需要手动提交事务，因此我们可以配合异常处理，去进行事务提交。**

> **注意 ！！！：以下代码是登录验证的示例代码，不是完整接口代码**
>
> ```python
> # 调用数据库连接工具，创建数据库连接，并获取连接对象和游标
> conn,cur = link_studyFlask()
> try:
>     # 创建sql
>     sql = """
>     INSERT INTO gitee_user (user_name, user_tel, user_pass, user_type) 
> 	VALUES ('john_doe', '12345678900', 'securepass', 2);
>     """
>     # 执行sql
>     cur.execute(sql)
> except Exception as e:      # sql执行失败, 捕捉异常
>     print("no")
> else:        # sql执行成功
>     conn.commit()      # 提交事务
>     print("yes")
> ```



## 3、完整的后端实现：

```python
项目目录介绍 - gitee_copy 项目的文件:

- gitee_copy 
    - link_mysql.py		【数据库链接工具代码】
    - user_port.py		【后端接口代码】
```

### `link_mysql.py`

```python
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
        'password': '123456',
        'db': 'study_flask',
        'charset': 'utf8'
    }
    # .connect() 是  pymysql 提供的用于创建连接的函数
    # 解包，将 字典中的 键值对，每个提取出来作为参数传递 ， 语法： **需要解包数据
    conn = pymysql.connect(**db_config)     # 连接成功后得到的是一个数据库连接对象
    cur = conn.cursor()       # 获取游标对象，用于对数据库中的数据进行操作工具
    return conn,cur      # 返回的元组数据
```

### `user_port.py`

```python
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

```

