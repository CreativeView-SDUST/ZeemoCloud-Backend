'''
Description: 
Author: Catop
Date: 2021-06-12 14:47:21
LastEditTime: 2021-06-12 16:15:21
'''
import json
import random
import string
from hashlib import md5

def enMd5(str):
    """md5加密"""
    ret = md5(str.encode('utf8')).hexdigest()
    
    return ret



def restRet(code, msg, body={}):
    """返回restful字符串"""
    ret = {}
    ret['code'] = code
    ret['msg'] = msg
    ret['body'] = ""
    if(len(body.keys()) > 0):
        ret['body'] = body
    
    ret_str = json.dumps(ret)

    return ret_str


def gen_token():
    """生成随机token"""
    random_str = ''.join(random.sample(string.ascii_letters + string.digits, 30))
    return random_str
