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

    # 在一的一方添加关联，
    # 这行代码表示和User模型发生了关联，增加了users属性
    # backref表示在关系的另一个模型中添加反向引用
    # backref='role' 表示role是User要用的一个属性，只不过定义定到这里了
    users = db.relationship('User', backref='role')

    # repr()方法显示一个可读字符串
    def __repr__(self):
        # 到时候打印Role的时候，可以打印下面的字符串
        return '<Role: %s %s>' % (self.name, self.id)


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    # 声明外键, 使用 表名.id 来标识外键 db.ForeignKey('roles.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    #


# 定义书和作者模型

# 作者模型
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    # 关系引用
    # books是给自己(Author模型)用的, author是给Book模型用的
    books = db.relationship('Book', backref='author')

    def __repr__(self):
        return "Author: %s" % self.name


# 书模型
class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

    # 定义外键
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self):
        return "Book: %s %s" % (self.name, self.author_id)


@app.route('/')
def hello_world():
    return render_template('books.html')



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
	
	# 生成数据
    au1 = Author(name='老王')
    au2 = Author(name='老惠')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()
    print(db.session)
    print('1')

    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # 将数据提交给会话
    db.session.add_all([bk1, bk2, bk3. bk4, bk5])
    # 提交会话
    db.session.commit()

    app.run(debug=True)