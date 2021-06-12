'''
Description: 
Author: Catop
Date: 2021-06-12 21:24:43
LastEditTime: 2021-06-12 22:04:56
'''
from flask import Blueprint, request, session
from hashlib import md5
import json
import common
import requests

photoApi = Blueprint('photo', __name__)

@photoApi.route('/get_random_photos', methods = ['POST'])
def get_random_photos():
    if(request.values.get('num')):
        num = request.values.get('num')
        num = int(num)
    else:
        num = 10

    #num = 10

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

    
    return str(ret_list)


if __name__ == '__main__':
    print(get_random_photos())