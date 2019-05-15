# FlaskItHeiMa
黑马程序员的免费 Flask课程

## Chapter 1

### 第一个Flask程序

#### 步骤如下
1. 导入Flask扩展
2. 实例化一个Flask程序
3. 定义路由以及对应的视图函数
4. 启动程序，将会使用Flask提供的一个小型服务器，用于测试

> 实例化一个Flask程序时需要传入一个参数，作用就是为了确定资源所在路径

> 视图函数可以返回两种内容：
> - 字符串
> - HTML模板文件，通过模板引擎来进行渲染，如果返回的是一个HTML模板引擎需要将对应的HTML文件存放到templates文件夹下，否则将会找不到对应的渲染文件


```python
# 导入Flask扩展
from flask import Flask
# 实例化一个Flask程序
app = Flask(__name__)

# 定义路由以及对应的视图函数
@app.route('/')
def index():
    return "<h1>hello flask</h1>"

# 启动程序
if __name__ == '__main__':
    app.run(debug=True)

```

### 路由请求方式限定

> 在定义路由以及对应的视图函数时，这里将会使用Python的装饰器来进行定义，Flask中定义路由是通过装饰器来实现的

> Flask中路由不指定methods属性时，默认是GET请求


```python

@app.route('/', methods=['GET', 'POST'])
def index():
    return '<h1>Hello World</h1>'

```

### 路由参数处理

> 有些时候，将会使用动态参数，例如订单页面我们会使用一个订单的Id号来区分不同订单的页面

> 使用<>定义一个路由的参数,<>内需要取一个名

```python
@app.route('/orders/<order_id>') # 这里对于order_id没有做限定，默认为string类型
# 路由参数处理,使用一个视图函数来显示不同用户的订单信息
def get_order_id(order_id):
    # 需要在视图函数()内传入参数名，那么后面的代码才可以使用
    return 'order_id %s' % order_id
    # 有的时候，需要对路由做优化，例如订单号必须为整数
    # <order_id> 改为 <int:order_id> 可以使用int 与 float类型
    # 如果指定了int, 将会对参数进行类型强制转换，如果转换成功就可以匹配
```



## Chapter 2

### 02-01 Jinji2模板引擎简介

> 视图函数的作用就是用来生成请求的响应

- 采用模板可以将视图与业务逻辑区分开来，便于项目的开发和维护
- 模板实质上就是一个响应文件，通过占位符来进行占位，来生成对应的动态内容
- 使用真实值来代替变量，并返回最终得到的字符串，这个过程称为‘渲染’

#### 使用模板的好处
1. 视图函数只负责业务逻辑和数据处理(业务逻辑方面)
2. 而模板则负责对处理好的数据进行展示(视图展示方面)
3. 代码结构清晰，耦合度低

#### 模板的使用
- 如何返回一个网页(模板)
- 如何使用模板填充数据

##### 返回一个网页
1. 在templates文件夹下新建一个html文件
2. 修改视图函数
```python
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
```

#####  使用模板填充数据

> render_template() 函数中，第一个参数是模板的文件名，后面的参数都是键值对，表示模板中对应变量的真实值，通常情况下两个名字保持一致

> {{ [] }} 来表示动态变量，也叫变量代码块kg

首先要将对应的视图函数映射为对应的模板，并且将要传入的内容通过参数进行传递
```python
@app.route('/home', methods=['GET', 'POST'])
def index():
    url_str = 'www.baidu.com'
    # 格式：模板中使用的名字=值
    return render_template('index.html', url_str=url_str)
```

接着，修改对应的html文件，使用{{ 模板中使用的名字 }} 来获取对应的值
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<p>这是一个段落</p>
{{ url_str }}
</body>
</html>

```

##### 变量代码块
{{ 变量名 }}

```python
@app.route('/list', methods=['GET', 'POST'])
def list():
    my_list = [1, 3, 5, 7, 9]
    # 格式：模板中使用的名字=值
    return render_template('lists.html', my_list=my_list)

@app.route('/dict', methods=['GET', 'POST'])
def dict():
    my_dict = {
        'name' : '黑马程序员'
    }
    # 格式：模板中使用的名字=值
    return render_template('dict.html', my_dict=my_dict)
```

模板文件中获取列表与字典中元素的值

```html
{{my_list}}
<!-- 获取列表元素的值 -->
{{my_list[0]}}
{{ my_list.2 }}

{{ my_dict }}
<!-- 获取字典元素的值 -->
{{ my_dict['name'] }}
{{ my_dict.name }}
```

##### 控制代码块

语法： {%  %}

for循环在html文件中遍历列表内容
```python

{# 遍历列表的内容 #}
{% for x in my_list %}
{{ x }} <br>
{% endfor %}
```

##### 过滤器的使用
| 代表过滤器

```python
{# 将url_str内容全部大写 #}
{{ url_str | upper }}
{{ url_str | reverse }}


```

过滤器可以链式调用：{{ url_str | upper | reverse }}

