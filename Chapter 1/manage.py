# coding:utf-8
# 1. 导入Flask扩展
from flask import Flask, render_template

# 2. 创建Flask应用程序实例，需要传入一个__name__，作用是为了确定资源所在的路径
app = Flask(__name__)


# 3. 定义路由以及视图函数
# 通过装饰器的形式来实现路由定义
# Flask中定义路由通过装饰器实现
# 路由默认是GET请求，如果希望其他请求可以使用methods参数进行指定
@app.route('/', methods=['GET', 'POST'])
def index():
    # 可以返回两种内容：1. 字符串内容 2. HTML模板内容，通过模板引擎负责渲染
    # return '<h1>你好，世界</h1>'
    # 如果返回一个HTML模板内容，必须存放于templates目录下，否则将会找不到文件
    return render_template('index.html')


# 使用<>定义一个路由的参数,<>内需要取一个名
@app.route('/orders/<order_id>') # 这里对于order_id没有做限定，默认为string类型
# 路由参数处理,使用一个视图函数来显示不同用户的订单信息
def get_order_id(order_id):
    # 需要在视图函数()内传入参数名，那么后面的代码才可以使用
    return 'order_id %s' % order_id
    # 有的时候，需要对路由做优化，例如订单号必须为整数
    # <order_id> 改为 <int:order_id> 可以使用int 与 float类型
    # 如果指定了int, 将会对参数进行类型强制转换，如果转换成功就可以匹配



# 4. 启动程序
# 将会运行起一个小型服务器（Flask提供的，用于测试的）
if __name__ == '__main__':
    app.run(debug=True)
