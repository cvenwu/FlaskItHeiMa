from flask import Flask, render_template, request, flash
app = Flask(__name__)
# app.config['SECRET_KEY'] = '123456'
app.secret_key = 'yirufeng'




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


@app.route('/form', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        # 原来需要自己去写的验证逻辑，下面一行代码就可以搞定
        # 3. 验证参数，WTF可以一句话实现校验
        # 提交的时候执行验证函数
        if login_form.validate_on_submit():
            # 如果能进入，说明验证成功
            flash('Success')
        # 验证不通过
        else:
            flash('Failed')

    # form就是将来模板中用到的变量
    return render_template('index.html', form=login_form)

"""
目的：实现简单的登录逻辑处理
1. 路由要有get和post两种请求方式------》判断请求方式
2. 获取请求的参数
3. 判断参数是否填写以及密码是否相同
4. 如果判断都没问题，我们就返回success
"""

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


if __name__ == '__main__':
    app.run(debug=True)