'''
Description: Flask主应用
Author: Catop
Date: 2021-06-12 13:05:13
LastEditTime: 2021-06-15 12:44:09
'''
import os
import common
from flask import Flask, session
from flask_cors import *
from datetime import timedelta
from api.user.views import userApi
from api.photo.views import photoApi


#蓝图注册
app = Flask(__name__)
app.register_blueprint(userApi, url_prefix='/user')
app.register_blueprint(photoApi, url_prefix='/photo')

#Flask配置
app.config['SECRET_KEY'] = os.urandom(24)   #随机sk
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)  # 会话配置7天有效
CORS(app, supports_credentials=True)    #允许跨域身份验证

@app.route("/")
def index():
    return "Welcome to ZeemoCloud!"

if __name__ == '__main__':
    host = common.config.FlaskConfig.host
    port = common.config.FlaskConfig.port
    debug = common.config.FlaskConfig.debug
    app.run(host=host,port=port, debug=debug)