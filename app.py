'''
Description: Flask主应用
Author: Catop
Date: 2021-06-12 13:05:13
LastEditTime: 2021-06-12 16:52:55
'''
import os
import common
from flask import Flask, session
from datetime import timedelta
from api.user.views import userApi



app = Flask(__name__)
app.register_blueprint(userApi, url_prefix='/user')

app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 配置7天有效


@app.route("/")
def index():
    return "Welcome to ZeemoCloud!"

if __name__ == '__main__':
    host = common.config.FlaskConfig.host
    port = common.config.FlaskConfig.port
    debug = common.config.FlaskConfig.debug
    app.run(host=host,port=port, debug=debug)