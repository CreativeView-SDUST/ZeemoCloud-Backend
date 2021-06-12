'''
Description: boto3对象存储api
Author: Catop
Date: 2021-06-12 20:45:33
LastEditTime: 2021-06-12 22:06:55
'''
from boto3.session import Session
import common
import boto3
import botocore
import warnings
warnings.filterwarnings("ignore", category=UnicodeWarning)

access_key = common.config.OSSConfig.access_key
secret_key = common.config.OSSConfig.secret_key
url = "https://eos-beijing-2.cmecloud.cn" #such as 'http://10.254.3.68:7480'
session = Session(access_key, secret_key)
s3 = session.resource('s3', endpoint_url=url)
s3_client = session.client('s3', endpoint_url=url)
BUCKET = 'zeemo'
OBJECT = 'your object'
DST_OBJ = 'your dest object of copy'
DATA = 'your local file'



def list_buckets_of_user():
    resp = s3_client.list_buckets()['Buckets']
    for bucket in resp:
        print(bucket['Name'])

def upload_file(remote_name, file_path):
    """上传本地文件到OSS"""
    #注意此处文件名为
    resp = s3_client.put_object(Bucket="zeemo", Key=remote_name, Body=open(file_path, 'rb').read())

if __name__ == '__main__':
    #list_buckets_of_user()
    upload_file()