import hashlib
import sys
import time
from urllib import parse

import pymssql
import requests


class Port_sales:
    def __init__(self, start_time, end_time, secret_key):
        self.start_time = start_time
        self.end_time = end_time
        self.secret_key = secret_key

    def get_sign(self):
        strs = ''
        self.param = {'flag': 'Testing', 'method': 'sales.getList',
                      'type': 'json', 'timestamp': int(time.time()),
                      'start_time': self.start_time,
                      'end_time': self.end_time
                      }
        tmp = sorted(self.param.keys())
        for i in tmp:
            strs += i + str(self.param[i])
        result = hashlib.md5(strs.encode(encoding='utf-8'))
        Res = result.hexdigest().upper()
        tmp = Res + self.secret_key
        tmp_key = hashlib.md5(tmp.encode(encoding='utf-8'))
        key = tmp_key.hexdigest().upper()
        return key

    def get_sales(self):
        base_url = 'http://two.erp.taoex.com/index.php/openapi/rpc/service/'
        param = {'flag': 'Testing', 'sign': self.get_sign(), 'method': 'sales.getList',
                 'type': 'json', 'timestamp': int(time.time()),
                 'start_time': self.start_time,
                 'end_time': self.end_time
                 }
        request_param = parse.urlencode(param).encode(encoding='utf-8')
        header = {'Content_Type': 'application/x-www-form-urlencoded;charset=utf-8'}
        response_orders = requests.post(base_url, data=request_param, headers=header)
        return response_orders.text

    '''
    def json2sql(self):
        list1 = []
        conn = pymssql.connect('WIN-8D5O9I2ISMB','emily','Yr5258800a','DBSource')
        cur = conn.cursor()
        cur.executr(""" if not exists(select * form sysobjects a where a.name = 'Orders')
        create table Orders(
            count nchar(25),
            iostock_price_num nchar(150),
            unit_cost_num nchar(25),
            iostock_id  nchar(255),
            iostock_bn  nchar(255),
            branch_bn nchar(255),
            branch_name nchar(255),
            bn nchar(255),
            name nchar(255),
            barcode nchar(255),
            nums nchar(255),
            balance_nums nchar(255),
            type nchar(25),
            iostock_time nchar(255),
            memo nchar(255),
            original_bn nchar(255),
            iostock_price nchar(255),
            unit_cost nchar(255))
        """)






            '''

if __name__ == '__main__':
    s = Port_sales('2020-03-03 00:00:00', '2020-04-03 19:30:00',
                    'egCFpcGpliNUyIDjtwjNhIJeBSWiSzYJ')  # sys.argv[1],sys.argv[2],sys.argv[3]
    print(s.get_sales())

