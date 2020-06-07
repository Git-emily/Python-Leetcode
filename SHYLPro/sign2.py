import json
import urllib

import urllib3.request
import requests
import pymssql
import hashlib
from urllib import request
import sys
import time


class Port_Iostock:
    #入口传参
    def __init__(self,secret_key):
        self.secret_key = secret_key

     #获取签名
    def get_sign(self):
        strs = ''
        self_param = {'flag': 'Testing', 'method': 'stock.getAll',
                    'type':'json',
                      'timestamp': int(time.time())
                      }
        tmp = sorted(self_param.keys())  # 按照key值排序
        for i in tmp:
            strs += i + str(self_param[i])  # 存储为字符串secret_key
        result = hashlib.md5(strs.encode(encoding='utf-8'))  # 将字符串加密
        Res = result.hexdigest().upper()  # 将字符串以字母/数字表示,并全部大写
        # 添加私钥
        temp = Res + self.secret_key
        tmp_key = hashlib.md5(temp.encode(encoding='utf-8'))
        key = tmp_key.hexdigest().upper()
        print('签名返回值：',key)
        return key

  #访问接口，并返回Json
    def get_Iostock(self,key):
        base_url = 'http://two.erp.taoex.com/index.php/openapi/rpc/service/'
        param = {'flag': 'Testing' ,'sign':key ,'method': 'stock.getAll',
                      'type': 'json',
                      'timestamp': int(time.time())
                      }
        request_param = urllib.parse.urlencode(param)
        print(request_param)

        header = {'Content-Type':'application/x-www-form-urlencoded;charset=utf-8'}
        response_iostock = requests.post(base_url, data = request_param, headers = header)  #post请求
        return  response_iostock.text

'''
    def json2sql(self,m):
        for d in m.json()['response']:
            print(d)
'''
if __name__ ==  '__main__':
    s = Port_Iostock('egCFpcGpliNUyIDjtwjNhIJeBSWiSzYJ')   #sys.argv[1],sys.argv[2],sys.argv[3]
    m = s.get_sign()
    print('返回text：',s.get_Iostock(m))
   # print(s.json2sql(m))