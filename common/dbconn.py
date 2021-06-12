'''
Description: 连接数据库
Author: Catop
Date: 2021-06-12 13:47:52
LastEditTime: 2021-06-12 16:31:42
'''
import pymysql
from common.config import DBConfig

#导入配置并创建连接
db_host = DBConfig.db_host
db_name = DBConfig.db_name
db_username = DBConfig.db_username
db_passwd = DBConfig.db_passwd

conn = pymysql.connect(host=db_host,user = db_username,passwd = db_passwd,db = db_name)


def db_init():
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    conn.ping(reconnect=True)

    return cursor


def list_user():
    """列出所有用户"""
    cursor = db_init()
    sql = "SELECT * FROM ZM_userinfo"
    cursor.execute(sql)
    ret = cursor.fetchall()
    
    return ret


def add_user(user_name, user_phone, user_passwd,user_type=""):
    """添加用户"""
    cursor = db_init()
    params = [user_name,user_phone,user_passwd,user_type]
    sql = "INSERT INTO ZM_userinfo(user_name,user_phone,user_passwd,user_type) VALUES(%s,%s,%s,%s)"
    cursor.execute(sql,params)
    uid = conn.insert_id()
    conn.commit()
    
    return uid

def get_user_info(phone):
    """根据手机号获取用户信息"""
    cursor = db_init()
    params = [phone]
    sql = "SELECT * FROM ZM_userinfo WHERE user_phone=%s"
    cursor.execute(sql,params)
    ret = cursor.fetchone()
    
    return ret



if __name__ == "__main__":
    #list_user()
    #print(add_user('catop','1234','8888'))
    print(get_user_info('13791681579'))