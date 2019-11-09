from flask import Flask
app = Flask(__name__, static_folder='', static_url_path='')


@app.route('/')
def hello_world():
    return 'Hello World!'
from routes.GoodsController import goodsController
app.register_blueprint(goodsController, url_prefix="/goods")

if __name__ == '__main__':

    app.run()
