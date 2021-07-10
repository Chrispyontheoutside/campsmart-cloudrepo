from flask import Flask

name=""
response=""
def run():
    app = Flask(__name__)
    @app.route('/')
    def hello_world():
        return '<h1>Hi, my name is'+name+'!</h1>'