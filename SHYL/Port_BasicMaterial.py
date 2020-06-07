import hashlib
import json
import sys
import time
from urllib import parse

import pymssql
import requests


class Port_basicmaterial:
    def __init__(self, page_no,page_size,secret_key):
        self.page_no = page_no
        self.page_size = page_size
        self.secret_key = secret_key

    def get_sign(self):
        strs = ''
        self_param = {'flag': 'Testing', 'method': 'basicmaterial.getList',
                      'type': 'json', 'timestamp': int(time.time()),
                      'page_no': self.page_no,'page_size': self.page_size
                      }
        tmp = sorted(self_param.keys())
        for i in tmp:
            strs += i + str(self_param[i])
        result = hashlib.md5(strs.encode(encoding='utf-8'))
        Res = result.hexdigest().upper()
        tmp = Res + self.secret_key
        tmp_key = hashlib.md5(tmp.encode(encoding='utf-8'))
        key = tmp_key.hexdigest().upper()
        return key

    def get_basicmaterial(self):
        base_url = 'http://two.erp.taoex.com/index.php/openapi/rpc/service/'
        param = {'flag': 'Testing', 'sign': self.get_sign(), 'method': 'basicmaterial.getList',
                 'type': 'json', 'timestamp': int(time.time()),
                 'page_no': self.page_no,'page_size': self.page_size
                 }
        request_param = parse.urlencode(param).encode(encoding='utf-8')
        header = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
        response_basicmaterial = requests.post(base_url, data=request_param, headers=header)
        return response_basicmaterial

    def json2sql(self):
        list1 = []
        conn = pymssql.connect('WIN-8D5O9I2ISMB','emily','Yr5258800a','DBSource')
        cur = conn.cursor()

        cur.execute(""" if not exists(select * from sysobjects a where a.name = 'Orders')
        create table Orders(
            No nchar(55),
            material_name nchar(255),
            material_bn nchar(150),
            material_spu nchar(255),
            visibled  nchar(25),
            serial_number  nchar(25),
            type nchar(25),
            cost nchar(255),
            retail_price nchar(255),
            weight nchar(255),
            unit nchar(255),
            specifications nchar(255),
            barcode nchar(255),
            count nchar(25))
        """)
        material_file = self.get_basicmaterial()
        responses =  json.loads(material_file.text)
        item1 = responses['response']
        item2 = item1['lists']
        for item3 in item2:
            #print(item3)
            sql_value = (item3,item2[item3]['material_name'],item2[item3]['material_bn']
                         ,item2[item3]['material_spu'],item2[item3]['visibled'],item2[item3]['serial_number']
                         ,item2[item3]['type'],item2[item3]['cost'],item2[item3]['retail_price']
                         , item2[item3]['weight'], item2[item3]['unit'], item2[item3]['specifications'], item2[item3]['barcode']
                         ,item1['count'])

            list1.append(sql_value)
        #print(list1)
        cur.execute("""truncate table Orders """)
        sql = "insert into Orders values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        cur.executemany(sql, list1)
        conn.commit()
        conn.close()

if __name__ == '__main__':
    s = Port_basicmaterial('1','100','egCFpcGpliNUyIDjtwjNhIJeBSWiSzYJ')  # sys.argv[1],sys.argv[2],sys.argv[3]
    s.json2sql()
    print('done')

