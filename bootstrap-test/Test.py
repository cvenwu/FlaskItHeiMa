from flask import Flask, render_template
# Python3这样导入flask扩展之bootstrap
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)



@app.route('/')
def index():


if __name__ == '__main__':
    app.run(debug=True)