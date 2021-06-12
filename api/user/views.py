'''
Description: 用户管理相关
Author: Catop
Date: 2021-06-12 13:09:25
LastEditTime: 2021-06-12 16:49:29
'''

from flask import Blueprint, request, session
from hashlib import md5
import json
import common


userApi = Blueprint('user', __name__)
 
 
@userApi.route('/', methods = ['POST'])
def user_index():

    return 'userapi'

@userApi.route('/register', methods = ['POST'])
def register():
    ret = ""
    try:
        user_name = request.values.get('username')
        user_phone = request.values.get('phone')
        user_passwd = request.values.get('passwd')

    except AttributeError:
        ret = common.tools.restRet(1,"参数不完整")
    else:
        exist_user_info = common.dbconn.get_user_info(user_phone)
        #判断手机号是否已注册过
        if(exist_user_info != None):
            ret = common.tools.restRet(1,"手机号已被注册")
        else:
            try:
                user_passwd = common.tools.enMd5(user_passwd)
                uid = common.dbconn.add_user(user_name,user_phone,user_passwd)  #主键id
            except:
                ret = common.tools.restRet(2,"内部错误")
            else:
                ret = common.tools.restRet(0,"注册成功！")

    return ret



@userApi.route('/login', methods = ['POST'])
def login():
    ret = ""
    try:
        user_phone = request.values.get('phone')
        user_passwd = request.values.get('passwd')
        
        user_info = common.dbconn.get_user_info(user_phone)
    except AttributeError:
        ret = common.tools.restRet(1,"参数不完整")
    except:
        ret = common.tools.restRet(2,"内部错误")
    else:
        if(common.tools.enMd5(user_passwd) == user_info['user_passwd']):
            ret = common.tools.restRet(0,"登录成功！")
            
            session['user_phone'] = user_phone
        else:
            ret = common.tools.restRet(1,"手机号或密码错误")
    
    return ret


@userApi.route('/status', methods = ['POST'])
def status():
    if(session.get('user_phone')):
        ret_info = {}
        try:
            user_info_all = common.dbconn.get_user_info(session.get('user_phone'))
        except:
            common.tools.restRet(2,"内部错误")
        else:
            ret_info['user_name'] = user_info_all['user_name']
            ret_info['user_phone'] = user_info_all['user_phone']
            
            return common.tools.restRet(0,"",ret_info)
        
    else:
        return common.tools.restRet(1,"您未登录")