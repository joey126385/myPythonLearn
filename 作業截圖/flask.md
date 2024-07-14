FLASK





# 【01】



# 【02】	項目配置



# 【03】	URL 與視圖

## 【0301】帶參數URL

將參數故掉到了PATH中

```python
#@app.route("/blog/<blog_id>")
@app.route("/blog/<int:blog_id>")
def blog_detail(blog_id):
    return  f"你訪問的博客是{blog_id}"
```



## 【0302】獲取查詢字串傳入參數

```python
from flask import Flask,request
```

```python
@app.route('/book/list')
def book_list():
    #arguments:參數
    #request.args  : 類參數
    page= request.args.get("page",default=1,type=int)
    return  f"你獲取的是第{page}的圖書列表"
```



# 【04】	Jinja2模板

```python
from flask import Flask,request,render_template
```

方式一 跳轉html

```python
@app.route("/")
def hello():
   # return "Hello, World!ddddddddddaaa"
    return  render_template("index.html")
```



方式二 帶參數

```python
@app.route("/blog/<blog_id>")
def blog_detail(blog_id):
   # return  f"你訪問的博客是{blog_id}"
   #把值傳入html
    return  render_template("blog.html",blog_id=blog_id)
```

```html
<body>
<h1>你訪問德柏克詳情視::{{blog_id}}</h1>
</body>
```



方式三 使用class 方式

```python
class User:
    def __init__(self,username,email):
        self.username=username
        self.email=email
```

```python
@app.route("/")
def hello():
   # return "Hello, World!ddddddddddaaa"
    #return  render_template("index.html")
    user=User(username="uuuu",email="jj@gmil.com")
    person={
           "username":"bbbb",
           "age":"22"
    }
    return render_template("index.html" ,user=user,person=person)
```

```html
<body>
首頁
<h1>{{user.username}}</h1>
<br>

<h1>{{person['username']}}</h1>
<h1>{{person.age}}</h1>
</body>
```



## 過濾器

```python
@app.route("/filter")
def filter_demo():
    user = User(username="uuuus", email="jj@gmil.com")
    return render_template("filter.html" ,user=user)
```

```html
<h1>{{user.username |length}}</h1>
```



## 字定義

```python
def datetime_format(value,format="%Y年 %m 月 %d 日 %H:%M"):
    return value.strftime(format)
```

```python
app.add_template_filter(datetime_format,"dformat")
```

```python
@app.route("/filter")
def filter_demo():
    user = User(username="uuuus", email="jj@gmil.com")
    mytime=datetime.now()
    return render_template("filter.html" ,user=user,mytime=mytime)
```

```html
<body>
<h1>{{user.username |length}}</h1>
<h2>{{mytime}}</h2>
<h2>{{mytime|dformat}}</h2>
</body>
```



## if語句

```python
@app.route("/control")
def control():
    age=19
    books=[
        {
        "name":"a book",
        "author":"author A"

        },
        {
            "name": "b book",
            "author": "author B"

        }
    ]
    return render_template("control.html",age=age,books=books)
```



```html
<body>
<div>
    {%   if age > 18 %}
    <div>滿18</div>
    {%   elif age ==18 %}
     <div>剛滿18</div>
    {%   else %}
     <div>未滿18</div>
    {% endif %}
</div>
{% for book in books %}
<div>圖書名稱:{{book.name}} 圖書作者:{{book.author}}</div>
{% endfor %}

</body>
```



## 模板繼承

```python
@app.route("/child1")
def child1():
    return render_template("child1.html")
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}{% endblock %}</title>
</head>
<body>
{% block body %}
{% endblock %}
</body>
</html>
```



套用模板

```html
{% extends "base.html" %}

{% block title %}
child1 title
{% endblock %}

{% block body %}
child1 body
{% endblock %}
```



## 加載靜態文件

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="{{ url_for('static' ,filename='css/style.css') }}">
    <script src="{{ url_for('static' ,filename='js/my.js') }}"></script>
</head>
<body>
<img src="{{ url_for('static' ,filename='images/1.jpg') }}" alt="">
</body>
</html>
```