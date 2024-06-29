# axios

以下为拓展知识

### 1、**什么是请求？响应？**

![image-20230905155042043](.\img\image-20230905155042043.png)

*浏览器和服务器是按照HTTP协议进行数据通信的。它规定了通信的步骤、格式以及双方应该如何交互。* 

### 2、请求响应分析

### 有域名版解析：

```python
https://search.bilibili.com/all?vt=03064303&keyword=薄荷&from_source=webtop_search&spm_id_from=333.1007&search_source=5

# 网址详情解析：
https://      安全传输协议 
search.bilibili.com       域名--》计算机ip + 端口（某个程序代号）
all       接口名 --》 资源请求地址（计算机某个程序上的一个功能名称）
?         分隔符号，后面是在请求过程中携带的参数
vt=03064303&keyword=薄荷&from_source=webtop_search&spm_id_from=333.1007&search_source=5      请求参数
```



### 无域名版解析：



![image-20221201224603497](./img/image-20221201224603497.png)

**通过 http 协议 访问 192.168.100.11 对应的计算机 中的端口为 8080 的服务（程序），hello 是 8080 代表的程序中的一个功能（接口）**

```
ip:

*.*.*.*
192.168.100.11 
127.0.0.1
```



#### 浏览器：

- 输入网址：`http://192.168.100.11:8080/hello`

  - 通过IP地址192.168.100.11定位到网络上的一台计算机

  - 通过端口号8080找到计算机上运行的程序

  - /hello是请求资源位置

    - 资源：对计算机而言资源就是数据。
  - web资源：通过网络可以访问到的资源（通常是指存放在服务器上的数据）
  
  > `192.168.100.11:8080/hello` ，意思是向ip为192.168.100.11的计算机中的8080端口程序，获取资源位置是/hello的数据

**比喻理解：**

​	***	http 假设是人与人之间的沟通规范，192.168.100.11  假设是银行的坐标地址，端口号8080 假设是银行的业务窗口，/hello就是业务窗口的某个业务。***       

#### 服务器：

​        服务器可以理解为数据处理、提供中心，**就像现实生活中的银行**

> - 接收到浏览器发送的信息（如：/hello）   **类似于银行接受到客户发起的取钱业务**
> - 在服务器上找到/hello的资源      **类似于从保险箱里面提取取钱的金额**
> - 把资源发送给浏览器        **类似于把取出来的钱给客户**
>



### 3、**总结：**

> 网络三要素：
>
> - IP  ：网络中计算机的唯一标识
> - 端口 ：计算机中运行程序的唯一标识
> - 协议 ：网络中计算机之间交互的规则
>
> **问题：浏览器和服务器两端进行数据交互，使用什么协议？**
>
> **答案：http协议** 、https协议





### 4、今天咱们课堂主要讲解GET、POST 请求

GET请求和POST请求都是HTTP协议中常用的两种请求方法，用于与服务器进行数据通信。它们在如何传递数据以及在何种情况下使用上有一些重要区别：

GET请求和POST请求的区别：

| 区别方式     | GET请求                                                      | POST请求                                         |
| ------------ | ------------------------------------------------------------ | ------------------------------------------------ |
| 请求参数     | 请求参数在请求行中。<br/>例：`/brand/findAll?name=OPPO&status=1` | 请求参数在请求体中                               |
| 请求参数长度 | 请求参数长度有限制(浏览器不同限制也不同)                     | 请求参数长度没有限制                             |
| 安全性       | 安全性低。原因：请求参数暴露在浏览器地址栏中。               | 安全性相对高                                     |
| 常用于       | 常用于从服务器获取数据，参数通过URL的查询字符串传递。        | 常用于向服务器提交数据，数据传递在请求的主体中。 |

选择使用哪种请求方法取决于具体的业务需求和用例。一般来说，如果只是获取数据而不修改服务器状态，使用GET请求是合适的。如果需要向服务器提交敏感信息或执行可能会改变服务器状态的操作，使用POST请求更安全。

------

**什么是协议？什么是ip？什么是端口？什么是接口？** **get 、 post**





正题开始：

## 一、什么是axios

**Axios是一个**基于Promise的**JavaScript库**（*Promise是JavaScript中用于处理异步操作的一种机制，它表示一个异步操作的最终结果。Promise可以有三种状态：pending（进行中）、fulfilled（已成功）和rejected（已失败）*。）

Axios用于发送HTTP请求。它可以在浏览器和Node.js环境中使用，并且具有许多功能，使得在客户端和服务器端进行数据通信变得更加简单和方便。

使用Axios可以更好地管理和处理HTTP请求，包括处理错误、设置请求超时、发送请求数据、接收响应数据等。它已经成为开发人员中广泛使用的HTTP请求库之一，并且在许多前端和后端项目中得到了广泛的应用。

## 二、使用场景

通常**用于网络请求的交互**，它**适用于前端和后端开发**，并且在许多不同的项目中都有应用。

```
软件组成：
前端 ：肉眼能看到的（浏览器上的网站、手机上的小程序、app）【html、css、js、Vue、AXIOS】
后端 ：程序肉眼看不到的部分（信息存储，数据计算，数据查询，数据处理）【python、mysql、爬虫、数据分析】

目前许多的软件公司，程序开发都是前后端分离开发的，前端开发前端的，后端开发后端的，在开发过程中，前端在html网页上预留前后端交互的地方，后端提供前后端交互的接口，axios就是用于前后端交互的技术。
```

发送HTTP请求：Axios可以用来发送各种类型的HTTP请求，包括GET、POST、PUT、DELETE等。无论是向服务器获取数据还是提交表单数据，Axios都可以处理。

```
拓展：

客户端 ： 提供给用户的操作界面。

当我们在客户端点击某一个操作按钮，其实会触发一个请求（发送请求），请求会顺着网络传递给服务器，服务器会去接受这个请求并处理（处理请求），处理完后进行返回请求结果（响应结果）。

服务器 ： 提供服务的机器。用来运行项目的电脑。

目前我们进行的axios操作就是实现，我们前端去向后端发送请求，并让后端响应结果，拿到后端响应的结果后，可以进行操作。
```



## 三、引入方式

1. 通过axios本地包导入（先要将工具包放到写代码的文件夹中）

   ```js
   <script src="axios.js"></script>
   ```

2. 通过cdn的方式引入**(不建议)**

   ```js
   <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
   ```



## 四、书写步骤

- 步骤一、创建请求对象

- 步骤二、请求方式

- 步骤三、请求接口地址

- 步骤四、请求数据

- 步骤五、请求结果处理

  

## 五、请求参数

| 参数       | 作用                                                    |
| ---------- | ------------------------------------------------------- |
| method     | 请求方式  默认为GET                                     |
| url        | 请求地址                                                |
| **data**   | **data是作为请求主体被发送的数据   只适用于`post`请求** |
| **params** | **是即将与请求一起发送的 URL 参数 适用`get`请求**       |
| timeout    | 请求时间                                                |
| .then()    | 回调函数 用于获取服务器返回的数据                       |
| catch      | 用于处理失败状态                                        |

```javascript
// 语法总结：

// POST请求语法 :
axios({
    method : "post",
    url : "接口地址",
    data : {     
        // data只适合携带 post请求参数
    }
}).then((res)=>{
    // 打印相应结果并进行操作
})


// GET请求语法 :
axios({
    method : "get",
    url : "接口地址",
    params : {     
        // params 只适合携带 get请求参数
    }
}).then((res)=>{
    // 打印相应结果并进行操作
})
```



## 六、使用接口对数据进行增删改查(后端项目已经上传到云上电脑，大家可远程调用)

接口文档（指的是对某一个服务器上某一个服务的具体功能的介绍）：http://43.136.104.16/axios

接口地址格式（不包含参数）：http://43.136.104.16:3002/接口名

1. ### 增 

   http://43.136.104.16:3002/xinzeng

   通过http协议，访问ip为43.136.104.16的服务器，中端口为3000的服务（程序），xinzeng 是这个程序的一个功能，这个功能能够实现用户新增。

   新增过程用post请求方式携带参数，这些参数是程序开发者早就设定好的，用人家的接口就得按照人家的要求传参。

   ```js
   axios({
       method : 'post',
       url : 'http://43.136.104.16:3002/xinzeng',
       data : {
           name : '周瑜',
           age : 18
       }
   }).then((res)=>{    // 处理成功的结果
       console.log(res.data.message);
   })
   ```

   

2. ### 删

   ```js
   axios({
       method : 'get',
       url : "http://43.136.104.16:3002/shanchu",
       params : {
           id : 253
       }
   }).then((res)=>{    // 处理成功的结果
       console.log(res.data.message);
   })
   ```

   

3. ### 改

   ```js
   axios({
       method : 'get',
       url : 'http://43.136.104.16:3002/xiugai',
       params : {
           id : 254,
           name : '不渝'
       }
   }).then((res)=>{    // 处理成功的结果
       console.log(res.data.message);
   })
   ```

   

4. ### 查

   ```js
   // alert("进行查询")
   axios({
       method : 'get',
       url : 'http://43.136.104.16:3002/chaxun'
   }).then((res)=>{    // 处理成功的结果
       console.log(res.data);
   })
   ```

**综合实例：**

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="vue.js"></script>
    <!-- 导入axios包 -->
    <script src="axios.js"></script>
    <!-- css 内部样式  -网页皮囊 -->
    <style>
        /* 去掉浏览器的白边 */
        body {
            padding: 0px;
            margin: 0px;
        }
        /* flex容器 */
        .box {
            display: flex;
            width: 100%;
            height: 100vh;     /*可视化高度*/
            background-color: palevioletred;
        }
        /* flex项目 */
        #div1 {
            margin: auto;   /*结合flex容器当中的代码可以实现居中效果*/
        }
        /* 设定输入框样式 */
        input {
            font-size: 30px;
        }
        /* 设定按钮样式 */
        button {
            font-size: 30px;
            background-color: grey;
            border-radius: 20%;
            color: white;
        }
    </style>
</head>

<body>
    <!-- html代码 -网页骨架   -->
    <div class="box">   
        <div id="div1">
            <h1>增删改查：</h1>
            <!-- 输入框都使用 v-model 进行了双向绑定，绑定到了挂载的Vue对象中data数据源中的键 -->
            <!-- 按钮都填了 @click点击事件，每个事件对应Vue对象方法区中的一个具体的函数 -->
            <input type="text" v-model="add_username" placeholder="请输入新增的用户昵称">
            <input type="text" v-model="add_age" placeholder="请输入新增的用户年龄">
            <button @click="add">增</button>
            <br><br>
            <input type="text" v-model="del_id" placeholder="请输入被删除的用户id">
            <button @click="del">删</button>
            <br><br>
            <input type="text" v-model="upd_username" placeholder="请输入修改后的用户昵称">
            <input type="text" v-model="upd_id" placeholder="请输入被修改的用户id">
            <button @click="upd">改</button>
            <br><br>
            <button @click="sel" style="background-color: black;">查</button>
            <br>
            <!-- 插值法，用于渲染挂载的Vue对象中data数据源中的数据 -->
            {{select_data}}
            <!-- v-for循环，用于遍历序列类型数据的 -->
            <li v-for="(x,index) in select_data" :key="index">{{x}}</li>
        </div>
    </div>

    <!-- js代码 -网页灵魂 -->
    <script>
        // 创建了一Vue对象并且挂载到了 id选择器为div1的盒子上
        new Vue({
            el: "#div1",
                //数据源
            data: {     
                del_id: null,
                add_username: null,
                add_age: null,
                upd_username: null,
                upd_id: null,
                select_data: null   // 用来存储查询到的数据合集  
            },
                // 方法区，函数区
            methods: {      
                add() {    //新增方法
                    axios({
                        method : 'post',
                        url : 'http://43.136.104.16:3002/xinzeng',
                        data : {
                            name : this.add_username,
                            age : this.add_age
                        }
                    }).then((res)=>{    // 处理成功的结果
                        console.log(res.data.message);
                    })
                },
                del() {   // 删除方法
                    axios({
                        method : 'get',
                        url : "http://43.136.104.16:3002/shanchu",
                        params : {
                            id : this.del_id
                        }
                    }).then((res)=>{    // 处理成功的结果
                        console.log(res.data.message);
                    })
                },
                upd() {   //修改方法
                    axios({
                        method : 'get',
                        url : 'http://43.136.104.16:3002/xiugai',
                        params : {
                            id : this.upd_id ,
                            name : this.upd_username
                        }
                    }).then((res)=>{    // 处理成功的结果
                        console.log(res.data.message);
                    })
                },
                sel() {   // 查询方法
                    axios({
                        methos : 'get',
                        url : 'http://43.136.104.16:3002/chaxun'
                    }).then((res)=>{    // 处理成功的结果
                        console.log(res.data);
                        this.select_data = res.data
                    })
                }
            }
        })

        /* 
            前后端交互需求：
                    ！！！注意：我们是以前端的角度去进行交互，而不是后端，咱们暂时没有学习后端。！！！
                    交互步骤：
                        -   步骤一、创建请求对象
                        -   步骤二、请求方式
                        -   步骤三、请求接口地址
                        -   步骤四、请求数据
                        -   步骤五、请求结果处理
            新增方法:
                    需求一：当在输入框输入了用户昵称和年龄后，点击新增按钮，能够实现用户新增
                    需求二：新增完后触发自动查询
            删除方法:
                    需求一：用户从输入框输入 用户 id 后，点击删除按钮，可以对该条信息进行删除操作
                    需求二：删除完后触发自动查询
            修改方法:
                    需求一：当用户输入 被更改用户 id 和 修改后的用户昵称信息后 ，点击修改按钮，能够修改成功
                    需求二：修改完后触发自动查询
            查询方法:
                    需求一：当用户点击查询按钮，能够查询的到目前服务器中保存的所有用户信息
        */
    </script>
</body>

</html>
```

