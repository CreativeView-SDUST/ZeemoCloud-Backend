'''
Description: Redis实现token分发和会话控制
Author: Catop
Date: 2021-06-12 16:01:28
LastEditTime: 2021-06-12 16:34:53
'''
import redis
import json
from common.config import RedisConfig

rs_host = RedisConfig.rs_host
rs_port = RedisConfig.rs_port
rs_db = RedisConfig.rs_db

rs = redis.StrictRedis(rs_host, rs_port, rs_db)


def new_info(token, dict):
    """写入新的token-info对"""
    dict_str = json.dumps(dict)
    ret = rs.set(token, dict_str)

    return ret

    
def get_info(token):
    """读取token对应信息"""
    dict_str = rs.get(token)
    ret = json.loads(dict_str)

    return ret