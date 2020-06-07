import hashlib
import json
import sys
import time
from urllib import parse
import requests

def get_sign(st,et):
    strs = ''
    self_param = {'flag': 'Testing', 'method': 'iostock.getList',
                  'type': 'json',
                  'timestamp': int(time.time()), 'start_time': st,
                  'end_time': et, 'page_no': '1',
                  'page_size': '100'
                  }
    tmp = sorted(self_param.keys())  # 按照key值排序
    for i in tmp:
        strs += i + str(self_param[i])  # 存储为字符串secret_key
    result = hashlib.md5(strs.encode(encoding='utf-8'))  # 将字符串加密
    Res = result.hexdigest().upper()  # 将字符串以字母/数字表示,并全部大写
    # 添加私钥
    temp = Res + 'egCFpcGpliNUyIDjtwjNhIJeBSWiSzYJ'
    tmp_key = hashlib.md5(temp.encode(encoding='utf-8'))
    key = tmp_key.hexdigest().upper()
    print('签名返回值：', key)
    return key,st,et

def get_Iostock(key,st,et):
    base_url = 'http://two.erp.taoex.com/index.php/openapi/rpc/service/'
    print('11')
    param =  {'flag': 'Testing','sign': key, 'method': 'iostock.getList',
                  'type': 'json',
                  'timestamp': int(time.time()), 'start_time': st,
                  'end_time': et, 'page_no': '1',
                  'page_size': '100'
                  }
    request_param = parse.urlencode(param).encode('utf-8')
    print(type(request_param))

    header = {'content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
    response_iostock = requests.post(base_url, data= request_param,headers=header)  # post请求
    return response_iostock.text


if __name__=='__main__':
    n,st,et = get_sign('2020-03-03 00:00:00','2020-04-03 19:30:00')#'2020-03-03 00:00:00','2020-04-03 19:30:00'
    print(get_Iostock(n,st,et))
