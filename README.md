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
----------------------

## Chapter 3


### 一个简单的登录处理

> 这里我们使用了flask中的request来对请求进行分析和处理，request用于获取请求的方式以及对应的数据

```python


```

### 模板中动态传递消息
> 有时我们希望可以在进行逻辑处理时，需要将问题呈现在模板中，此时也是可以的

> 使用flash给模板传递消息


```python

@app.route('/', methods=['GET', 'POST'])
def index():
    # request：请求对象，--》用于获取请求的方式以及对应的数据
    # 1. 判断请求方式
    if request.method == 'POST':
        # 2, 获取请求参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        # 3. 判断参数是否填写 & 密码是否相同
        if not all([username, password, password2]):
            # print("参数不完整")
            flash("参数不完整")
        elif password != password2:
            # 此时表示参数填写不完整并且密码也不相同
            # print("密码不一致")
            flash("密码不一致")
        else:
            flash("SUCCESS")
            # return 'SUCCESS'

        # return '%s %s %s' % (username, password, password2)

    return render_template('index.html')
```

```html

<form action="" method="post">
        <label for="">用户名:</label><input type="text" name="username"><br>
        <label for="">密码:</label><input type="password" name="password" id=""><br>
        <label for="">确认密码:</label><input type="password" name="password2"><br>
        <input type="submit" value="提交"><br>
        {# 使用遍历获取闪现的消息 #}
        {% for message in get_flashed_messages() %}
            {{ message }}
        {% endfor %}
    </form>
```



#### Flask 使用消息闪烁（flash）报错：
> 使用flask传递消息的时候，flask希望消息是保密的，消息需要加密，需要设置SECRET_KEY,做加密消息的混淆
Flask 使用消息flash报错：The session is unavailable because no secret key was set

解决方法:设置Flask实例的SECTET_KEY属性。代码如下：
```python
from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'

```


#### 编码问题

> 当使用中文时编码出现问题，我们可以在字符串前面加上u
``` python
flash(u"密码不一致")
```



### WTF简介

#### 在HTML中使用表单


```html
    <form action="" method="post">
        <label for="">用户名:</label><input type="text" name="username"><br>
        <label for="">密码:</label><input type="password" name="password" id=""><br>
        <label for="">确认密码:</label><input type="password" name="password2"><br>
        <input type="submit" value="提交"><br>
    </form>
```

#### 使用Flask-WTF实现表单

> 需要自定义表单类，使用WTF实现表单

1. 自定义表单类，每个标签内容，以及对应的验证函数
2. 编写对应表单的视图界面
3. 编写业务逻辑



```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
class LoginForm(FlaskForm):
    # 代表我们的用户名输入框
    # validators是一个列表
    # DataRequired()是一个函数
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField(label='密码', validators=[DataRequired()])
    # EqualTo() 中有2个参数，第1个参数指定和谁进行比较，第2个参数是message，指示出错如何处理
    password2 = PasswordField(label='确认密码', validators=[DataRequired(),
                                            EqualTo('password', message='密码填入不一致')])
    submit = SubmitField('提交')
```

**CSRF是跨站请求伪造**，如果在验证的时候没有csrt_token将会报错，

```python
<form action="" method="post">
        {# 设置csrf_token #}
        {{ form.csrf_token() }} {# 跨站请求伪造，没有这行代码会报错 #}
        {{ form.username.label }} {{ form.username }} <br>
        {{ form.password.label }} {{ form.password }} <br>
        {{ form.password2.label }} {{ form.password2 }} <br>
        {{ form.input }} <br>
</form>

```


使用flask中的wtf验证，除了可以帮助我们验证逻辑之外，还可以帮助我们验证没有编写的业务逻辑，所以，下面业务代码将会报错


验证函数可以写多个，是一个列表

### WTF表单显示

### WTF表单验证

------

## Chapter 4

### Flask-SQLAlchemy 扩展
> SQLAlchemy是对数据库的抽象，通过ORM映射使得我们不用编写SQL语句，其实也是通过Python的面向对象的思想来操作数据库

> SQLAlchemy 是一个关系型数据库框架，它提供了高层的ORM和底层原生数据库的操作，flask-sqlalchemy是一个简化了的SQLAlchemy操作的flask扩展

#### 使用Flask-SQLAlchemy管理数据库


使用步骤：
1. **导入扩展**：from flask_sqlalchemy import SQLAlchemy
2. 配置
3. 创建SQLAlchemy对象

> 注意：连接之前确保连接的数据库已经存在

```python
# 导入扩展
from flask_sqlalchemy import SQLAlchemy
# 数据库名称://用户名:密码@ip地址/数据库名
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/flask_sql_demo'
# 创建SQLAlchemy对象，创建的时候传入app
db = SQLAlchemy(app)

```


### 定义数据模型

> 在前面我们配置好数据库连接之后，接下来就可以使用SQLAlchemy对数据库进行操作，通过面向对象的思维来操作数据库

步骤：
1. 每张表对应一个模型类，编写对应的模型类
2. 创建表
```python
# 创建表之前删除已有的表格
db.drop_all()
# 实际生产环境中使用命令行迁移的方式来创建表
db.create_all()

```

例如下面的两张表格roles与users
roles字段: id(主键) name
users字段：id(主键) name role_id(外键)

**当我们创建一个类的时候，如何会把普通类当做SQLAlchemy中的模型处理：每个类需要继承db.Model**

**定义外键的时候需要使用 表名.字段名 指定**
```python

'''
两张表：角色(管理员/普通用户)
      用户(角色ID)
'''
# 如何才能把类当做模型去处理：需要继承db.Model才会被当做模型处理
class Role(db.Model):
    # 定义表和字段
    ## 定义表名
    __tablename__ = 'roles'
    ## 定义字段,db.Column就表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    ## 定义长度为16字节的name
    name = db.Column(db.String(16), unique=True)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 声明外键, 使用 表名.id 来标识外键 db.ForeignKey('roles.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
```

#### SQLAlchemy中字段类型与python对应的字段类型

类型名 | python中的数据类型 | 说明
Integer | int | 普通整数，一般是32位

#### 常用的SQLAlchemy列选项

#### 常用的SQLAlchemy关系选项
<table><th><tr><td>选项名</td><td>说明</td></tr></th><tbody>
        <tr><td>backref</td><td>在关系的另一模型中添加反向引用</td></tr>
        <tr><td>primary join</td><td>明确指定两个模型之间使用的联结条件</td></tr>
        <tr><td>uselist</td><td>如果为False,不使用列表，而是用标量值</td></tr>
        <tr><td>order_by</td><td>指定关系中记录的排序方式</td></tr>
        <tr><td>secondary</td><td>指定多对多记录的排序方式</td></tr>
        <tr><td>secondary join</td><td>在SQLAlchemy中无法自行决定时，指定多对多关系中的二级联结条件</td></tr>
</tbody>
</table>


### 数据库的基本操作
> 在SQLAlchemy中，插入、修改、删除操作都交给数据库会话进行管理


#### 基本概念
会话使用db.session进行表示，在准备把数据写入到数据库之前，需要添加到会话并且使用commit()方法提交会话
SQLAlchemy中，查询操作是通过query对象操作数据。**最基本的查询会返回所有数据，可以通过过滤器实现更精确的数据查询**

```python
db.session.add(role) # 添加到数据库的session中
db.session.add_all([user1, user2]) # 添加多个信息到session中
db.session.commit() # 提交数据库的修改
db.session.rollback() # 数据库的回滚操作
db.session.delete() # 删除数据库(需跟上commit)

```

####  添加数据
> 可以使用add_all() 传入一个列表参数来添加多个数据

```python
# 插入一个角色
    role = Role(name='yirufeng')
    db.session.add(role)
    db.session.commit()

    # 插入一个用户名
    user = User(name='itheima', role_id=role.id)
    db.session.add(user)
    db.session.commit()
```


#### 修改数据


```python
 # 修改用户的属性, 添加只添加一次就可以了，剩下的直接修改之后commit就可以了
    user.name = 'chengxuyuan'
    db.session.commit()
```

#### 删除数据


```python
# 删除用户
    db.session.delete(user)
    db.session.commit()
```


完整代码如下：
```python

from flask import Flask, render_template
# 导入sqlalchemy扩展
from flask_sqlalchemy import SQLAlchemy

import pymysql


app = Flask(__name__)
app.secret_key = '123456'

# 下面一行代码是Flask的数据库设置
# 数据库名称://用户名:密码@ip地址/数据库名
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost:3306/flask_sql_demo'
# 下面一行代码是Flask动态追踪修改设置，如果未设置只会提示警告，并不会报错
# 如果启用动态追踪修改设置，将会消耗部分性能，并且在未来版本中会移除掉
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost:3306/movie"

db = SQLAlchemy(app)



'''
两张表：角色(管理员/普通用户)
      用户(角色ID)
'''
# 如何才能把类当做模型去处理：需要继承db.Model才会被当做模型处理
class Role(db.Model):
    # 定义表和字段
    ## 定义表名
    __tablename__ = 'roles'
    ## 定义字段,db.Column就表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    ## 定义长度为16字节的name
    name = db.Column(db.String(16), unique=True)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 声明外键, 使用 表名.id 来标识外键 db.ForeignKey('roles.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # 首先删除数据库的所有表
    db.drop_all()
    # 其次创建数据库中所需要的表
    db.create_all()

    # 插入一个角色
    role = Role(name='yirufeng')
    db.session.add(role)
    db.session.commit()

    # 插入一个用户名
    user = User(name='itheima', role_id=role.id)
    db.session.add(user)
    db.session.commit()

    # 修改用户的属性, 添加只添加一次就可以了，剩下的直接修改之后commit就可以了
    user.name = 'chengxuyuan'
    db.session.commit()

    # 删除用户
    db.session.delete(user)
    db.session.commit()


    app.run(debug=True)

```


### 模型之间的关联

#### 一对多


比如User希望有role属性，但是这个属性的定义需要在另一个模型中定义

> 在一的一方添加关联
users = 




### 数据库查询操作

例子：
1. 查询全部用户：User.query.all()
2. 查询有多少个用户：User.query.count()
3. 查询第一个用户：User.query.first()
4. 查询id为4的用户：User.query.get(4)
5. 查询id为4的用户：User.query.filter_by(id=4).first()
6. 查询id为4的用户：User.query.filter(User, id==4).first()
7. 查询id为4的用户：User.query.filter_by(id=4).first()


**filter_by 格式： 属性=值**
**filter格式： 属性==值** filter功能更加强大，可以实现更多的查询条件，支持比较运算符

#### 查询过滤器
> 查询过滤器用于对数据进行筛选，

#### 查询执行器
> 查询执行器用于执行查询操作

### 综合案例之图书管理