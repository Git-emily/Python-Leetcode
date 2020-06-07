import json
import requests
import pymssql
import hashlib
from urllib import request, parse
import sys
import time
from collections import abc


class Port_Iostock:
    #入口传参
    def __init__(self,start_time,end_time,secret_key):
        self.start_time = start_time
        self.end_time = end_time
        self.secret_key = secret_key

     #获取签名
    def get_sign(self):
        strs = ''
        self_param = {'flag': 'Testing', 'method': 'iostock.getList',
                    'type':'json',
                      'timestamp': int(time.time()), 'start_time': self.start_time,
                      'end_time': self.end_time,'page_no': '1',
                      'page_size': '100'
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
        return key

  #访问接口，并返回Json
    def get_Iostock(self,key):
        base_url = 'http://two.erp.taoex.com/index.php/openapi/rpc/service'
        param = {'flag': 'Testing' ,'sign':key,'method': 'iostock.getList',
                      'type': 'json',
                      'timestamp': int(time.time()), 'start_time': self.start_time,
                      'end_time': self.end_time, 'page_no': '1',
                      'page_size': '100'
                      }
        request_param = parse.urlencode(param).encode('utf-8')

        print(type(request_param))

        header = {'Content-Type':'application/x-www-form-urlencoded;charset=utf-8',
                  'Connection': 'keep-alive'}

        response_iostock = requests.post(base_url, data = param, headers = header)  #post请求

        return  response_iostock.content

'''
    def json2sql(self,m):
        for d in m.json()['response']:
            print(d)
'''
if __name__ ==  '__main__':
    s = Port_Iostock('2020-03-03 00:00:00','2020-04-03 19:30:00','egCFpcGpliNUyIDjtwjNhIJeBSWiSzYJ')   #sys.argv[1],sys.argv[2],sys.argv[3]
    m = s.get_sign()
    print('返回text：',s.get_Iostock(m))
   # print(s.json2sql(m))