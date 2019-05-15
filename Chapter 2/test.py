from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>hello flask</h1>"

@app.route('/home', methods=['GET', 'POST'])
def index2():
    url_str = 'www.baidu.com'
    # 格式：模板中使用的名字=值
    return render_template('index.html', url_str=url_str)

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

if __name__ == '__main__':
    app.run(debug=True)