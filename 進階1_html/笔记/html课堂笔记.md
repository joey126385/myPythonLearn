### HTML

### 一、什么是HTML？

标签库（积木库）

HTML的全称为超文本标记语言，是一种[标记语言](https://baike.baidu.com/item/标记语言/5964436?fromModule=lemma_inlink)。它包括一系列标签，通过这些标签可以将网络上的文档格式统一。

简单来说，网页就是用HTML语言制作的。HTML是一门描述性语言，是一门非常容易入门的语言。

课外拓展地址：[HTML5 简介 (w3school.com.cn)](https://www.w3school.com.cn/html/html5_intro.asp)

​                          [HTML 教程 | 菜鸟教程 (runoob.com)](https://www.runoob.com/html/html-tutorial.html)

### 二、HTML的作用

用来开发网页。

### 三、网页的组成部分

网页，浏览器打开的一个页面。

网站，浏览器打开的，由很多网页组成的一个整体。

![image-20230625202100944](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230625202100944.png)

**网页由`HTML`+`CSS`+`js`组成**

- `HTML`:网页的骨架【确定网页的组成元素】
- `CSS`：网页的颜色 【能够让网页炫酷好看起来，可以结合`html`控制网页排版，或者网页内容颜色样式】
- `js`：网页的动作【`javaScript` 能够让网页实现复杂的逻辑】

### 四、工具介绍

`python`开发推荐推荐工具`pycharm`

`pycharm`也可以用来写`html`

### 五、结构介绍

1. 生成结构

   `pycharm`会自动帮我们生成`html`结构

   
   
2. 结构详情介绍

   ![image-20230623154259276](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230623154259276.png)
   
   - `html`由标签和属性构成。
   - 标签：长在尖角号后面的第一个单词就是标签
   - 属性：长在标签后面的并且用空格隔开的，称作 属性
   - 结构标签介绍
   
   ```html
   <!-- 文档类型声明 -->
   <!DOCTYPE html>
   <!-- 告诉浏览器整个文档的内容是用英语编写的。这有助于浏览器更好地理解和处理文档内容。-->
   <html lang="en">
   
   <!-- 语法规范一：所有标签都用< >包裹-->
   <!-- 语法规范二：所以的标签要不是包含关系，要么是同级关系 -->
       
   <!-- head包裹的称为头部区域 -->
   <head> 
     <!-- 网页采用utf-8的编码格式 -->
     <meta charset="UTF-8"> 
     <!-- 用于设置网页的视口（viewport）和浏览器兼容性。-->
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <!-- 网页标题 -->
     <title>Document</title>
   </head>
       
   <!-- body包裹的称为内容区域 -->
   <body> 
   </body>
       
   </html>
   ```
   
   > 拓展注释：
   
   > ```html
   > 之后我们可能还会看到以下类型的源码:
   > 
   > <!-- 用于设置网页的视口（viewport）和浏览器兼容性。-->
   >   <meta http-equiv="X-UA-Compatible" content="IE=edge">
   > <meta name="viewport" content="width=device-width, initial-scale=1.0">
   > 以上这些是HTML的<meta>标签，通常用于为浏览器提供有关页面如何显示和呈现的额外信息。让我为你解释这两个标签的含义：
   > 
   > 
   > <meta http-equiv="X-UA-Compatible" content="IE=edge">
   > 这个标签是为了确保网页在Internet Explorer中以最高的渲染模式呈现。X-UA-Compatible是一个HTTP响应头，也可以作为<meta>标签放在HTML中。content="IE=edge"指示Internet Explorer使用其最新的渲染模式（即“edge”模式）来显示内容，而不是使用旧版本的兼容模式。这有助于确保网页在IE中的显示与其他现代浏览器一致。
   > 
   > 
   > <meta name="viewport" content="width=device-width, initial-scale=1.0">
   > 这个标签是为了确保网页在移动设备上正确显示。viewport是一个用于控制页面布局和缩放的元标记。
   > * `width=device-width`：这意味着页面的宽度应该与设备的屏幕宽度相同，从而防止页面内容在移动设备上被缩放或拉伸。
   > * `initial-scale=1.0`：这设置了页面的初始缩放级别为100%，即不缩放。
   > 这些标签通常被放置在HTML文档的<head>部分，以帮助确保网页在各种设备和浏览器上都能正确和一致地显示。
   > ```
   
   

### 四、网页中常见的标签

1. 标题标签

   - h1标签
   - h2标签
   - h3标签
   - h4标签
   - h5标签
   - h6标签

   代码演示：

   ```html
   <body>
     <h1>hello word</h1>
     <h2>hello word</h2>
     <h3>hello word</h3>
     <h4>hello word</h4>
     <h5>hello word</h5>
     <h6>hello word</h6>
   </body>
   ```

   

2. 段落标签

   一般用来写文章段落

   - p标签

     ```html
     <body>
       <p>
         这是一段优美的文章
       </p>
     </body>
     ```

3. 强调标签

   - em标签：
     - 作用：倾斜
   - b标签：
     - 作用：加粗

   代码演示：

   ```html
   <body>
     你们真<em>帅</em>
     你们真<b>帅</b>
   </body>
   ```

4. br换行标签

   - br标签

   代码演示：

   ```html
   <body>
     窗前明月光<br>疑是地上霜<br>举头望明月<br>低头思故乡
   </body>
   
   注意，br标签为单个标签
   ```

5. hr标签

   - hr标签
     - 作用：标签变成分割线

   代码演示：

   ```html
   <body>
     你好呀
     <hr>
     哈哈
   </body>
   
   注意，hr标签为单个标签
   ```

6. **div标签**

   - div标签  是用来布局的，并没有语义，只是一个区块

   - div标签是一个块级标签（不管内容多少，即使内容不满一行它也会**自动换行**）

     ```html
     <body>
       <div>
         这是个盒子
       </div>
     </body>
     ```

7. **span标签**

   - 没有语义，一般用来包裹文字,让文字更好被选中。

   - span标签是行级块标签（是否换行跟内容有关，**不会主动换行**）

     ```html
     <body>
         <span>这是个盒子</span>
     </body>
     ```

8. img标签(图片标签)

   - 作用：插入图片
   - 属性
     - **src: 引入图片路径**
     - alt: 对图片的描述
     - height: 设置图片的高
     - width: 设置图片的宽度

   ***注意：一定要设置src***

   代码演示：

   ```html
   // 可以链接引入
   <img src="https://www.runoob.com/wp-content/uploads/2013/06/image-icon.png" alt="">
   // 也可以本地引入
   <img src="./图片.png" alt="">
   ```
   
9. a标签

   - 作用:点击跳转到另一个网页
   - **href属性：指定访问资源的URL**
   - target属性:指定打开资源的方式
     - _self：默认值，在当前页面打开
     - _blank：在其他页面打开

   代码示例：

   ```html
   <body>
     <a href="https://www.w3school.com.cn/">点我进入w3cSchool</a>
     <a href="https://baidu.com" target="_blank">点击重新打开页面跳转到百度</a>
   </body>
   ```

10. 列表标签

   - 有序列表 ol li

     ```html
     <body>
       <ol>
         <li>1</li>
         <li>1</li>
         <li>1</li>
         <li>1</li>
       </ol>
     </body>
     ```

   - 无序列表 ul li

     ```html
     <body>
       <ul>
         <li>1</li>
         <li>1</li>
         <li>1</li>
         <li>1</li>
       </ul>
     </body>
     ```



11. **表单标签**

    在网页中主要负责数据采集功能

    `type`属性用于定义`<input>`元素的类型。该属性指定了输入字段所期望的数据类型或输入方式。

    - **`text`：文本输入字段，用于输入纯文本内容。**
    - **`password`：密码输入字段，输入的内容会被隐藏，通常以圆点或星号显示。**
    - **`email`：电子邮件地址输入字段，用于输入符合电子邮件格式的邮箱地址。**
    - `number`：数字输入字段，用于输入数值。
    - **`date`：日期输入字段，用于选择或输入日期。**
    - **`checkbox`：复选框，用于选择多个选项。**
    - **`radio`：单选按钮，用于选择单个选项。**
    - `file`：文件上传字段（按钮），用于选择上传文件。
    - **`submit`：提交按钮，用于提交表单数据。**
    - **`reset`：重置按钮，用于将表单字段重置为默认值。**
    - **`button`：普通按钮，用于执行自定义的JavaScript操作。**

    `placeholder`属性：用于在输入字段中提供默认提示文本。

    - text: 默认值、定义单行输入字段

      ```html
      <body>
        <input type="text" placeholder="请输入姓名">
      </body>
      ```
    
    - password：定义密码字段
    
      ```html
      <body>
        <input type="password"  placeholder="请输入密码">
      </body>
      ```
    
    - radio：定义单选框（拓展）
    
      ```html
      <!--单选框-->
      <!--想要多个单选按钮互斥，需要把他们的name设为一样的-->
      <body>
           <h3>题目1：请问html是什么？（单选）</h3>
      <!--     假设这是一个题目，题目有三个选项，name就是题目名字，而下面三个选择框是属于这个题的。
      		 只要是name的值是一致的，他们就属于同一个组织。
      -->
           <input type="radio" name="题目1">
           <span>A.后端语言</span>
           <br>
          <input type="radio" name="题目1">
           <span>B.数据库语言</span>
           <br>
          <input type="radio" name="题目1">
           <span>C.前端标签库</span>
           <br>
      </body>
      ```
    
    - checkbox：复选框（拓展）
    
      ```html
      <body>
           <h3>题目2：请问html是什么？（多选）</h3>
          <!--  注意：使用单选框和复选框，记得一定要为单选框或者复选框绑定组织。只要是name的值是一致的，他们就属于同一个组织。
          -->
          <input type="checkbox" name="题目2">
               <span>A.数据库语言</span>
           <br>
          <input type="checkbox" name="题目2">
               <span>B.超文本标记语言</span>
           <br>
          <input type="checkbox" name="题目2">
               <span>C.前端标签库</span>
           <br>
      </body>
      ```
    
    - button: 按钮
    
      ```html
      <!--按钮-->
        <input type="button" value="一个普通按钮">
        <button>一个普通按钮的第二个写法</button>
      ```
    
    - reset: 重置 会将表单的数据清楚
    
      ```html
      <!--重置按钮-->
      <input type="reset" value="重置">
      ```
    
    - submit：提交按钮 会把表单数据发送到服务器
    
      ```html
      <!--注册按钮-->
      <input type="submit" value="注册">
      ```
    
    - file：会将头像文件上传
    
      ```html
      <!--上传文件-->
      <input type="file"><br>
      ```
    
    
    - select :定义下拉列表，option定义列表项
    
      ```html
      <body>
        <select>
          <option value="1">红色</option>
          <option value="2">绿色</option>
          <option value="3">黄色</option>
        </select>
      </body>
      ```
    
      

# 课后作业（复刻这个网页部分，复刻80%左右就行，不用一模一样，如果实现不了的部分可以放截图）：

![image-20240318214709387](.\作业.png)

```python
以上图片来源于：https://www.runoob.com/html/html-tutorial.html
```

