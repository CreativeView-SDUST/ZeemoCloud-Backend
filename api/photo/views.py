'''
Description: 
Author: Catop
Date: 2021-06-12 21:24:43
LastEditTime: 2021-06-15 13:00:23
'''
from flask import Blueprint, request, session
from hashlib import md5
import datetime
import json
import common
import requests

photoApi = Blueprint('photo', __name__)

@photoApi.route('/get_random_photos', methods = ['POST'])
def get_random_photos():
    """获取随机图片"""
    ret = ""
    if(request.values.get('num')):
        num = request.values.get('num')
        num = int(num)
    else:
        num = 10

    ret_list = []
    
    for i in range(0,num):

        if(i%3 == 0):
            res = requests.get("https://api.ixiaowai.cn/api/api.php?return=json",verify=False)
            text = res.text  
            res_dict = json.loads(text.encode('utf8')[3:].decode('utf8'))

            if(res_dict['code'] == '200'):
                img_info = {}
                img_info['img_name'] = 'foo'
                img_info['img_url'] = res_dict['imgurl']
                img_info['width'] = res_dict['width']
                img_info['height'] = res_dict['height']
                
                ret_list.append(img_info)
        else:
            ret_list.append(ret_list[i-1])
    ret_dict = {}
    ret_dict['img_num'] = num
    ret_dict['img_list'] = ret_list

    ret = common.tools.restRet(0,"success",ret_dict)

    return ret


@photoApi.route('/save_photo', methods = ['POST'])
def save_photo():
    """保存图片信息到数据库"""
    ret = ""
    #从会话获取用户信息
    if(session.get('user_phone')):
        user_phone = session.get('user_phone')
        try:
            user_info = common.dbconn.get_user_info(session.get('user_phone'))
            img_name = request.values.get('img_name')
            if(user_info):
                #已注册用户
                dt=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                common.dbconn.save_photo_info(user_phone,img_name,dt)
        except AttributeError:
            ret = common.tools.restRet(1,"参数不完整")
        except:
            ret = common.tools.restRet(2,"内部错误")
        else:
            ret = common.tools.restRet(0,"保存成功")
    else:
        ret = common.tools.restRet(1,"用户未登录")
    
    return ret

if __name__ == '__main__':
    print(get_random_photos())