import hashlib
import json
import sys
import time
from urllib import parse

import pymssql
import requests

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
                      'end_time':self.end_time, 'page_no': '1',
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
    def get_Iostock(self):
        base_url = 'http://two.erp.taoex.com/index.php/openapi/rpc/service/'
        param = {'flag': 'Testing', 'sign': self.get_sign(), 'method': 'iostock.getList',
                 'type': 'json',
                 'timestamp': int(time.time()), 'start_time': self.start_time,
                 'end_time': self.end_time, 'page_no': '1',
                 'page_size': '100'
                 }
        request_param = parse.urlencode(param).encode('utf-8')
        print('参数是：',request_param)
        header = {'content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}

        response_iostock = requests.post(base_url, data= request_param,headers=header)
        return response_iostock

    def json2sql(self):
        list1 = []
        #链接数据库
        conn = pymssql.connect('WIN-8D5O9I2ISMB','emily','Yr5258800a','DBSource')
        cur = conn.cursor()  #创建游标对象，sql语句的执行基本都在游标上
    

        #创建数据库表
        cur.execute("""if not exists(select * from sysobjects a where a.name = 'Iostock')
            create table IoStock(
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
            unit_cost nchar(255)
            ) """)  #三引号的作用，将字符串原样复制

    #获取json文件
        Iostock_file = self.get_Iostock()
        print('response:',Iostock_file.text)
        print('开始解析')
        responses = json.loads(Iostock_file.text)   #response为dict
        #print(type(responses))
        #print('response值:',responses)
        item1  = responses['response']
        #print(type(item1))
        for item2 in item1['lists']:
            sql_value = (item1["count"],item1["iostock_price_num"],item1["unit_cost_num"]
                      ,item2["iostock_id"],item2["iostock_bn"],item2["branch_bn"],item2["branch_name"],item2["bn"],item2["name"],
                        item2["barcode"],item2["nums"],item2["balance_nums"],item2["type"],item2["iostock_time"],
                         item2["memo"],item2["original_bn"],item2["iostock_price"],item2["unit_cost"])

            list1.append(sql_value)
        #print('list1', list1)

        #向SQL SER插入数据
        sql = "insert into IoStock values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        cur.executemany(sql,list1)

        conn.commit()
        conn.close()

if __name__ ==  '__main__':
    s = Port_Iostock('2020-03-03 00:00:00','2020-04-03 19:30:00','egCFpcGpliNUyIDjtwjNhIJeBSWiSzYJ')   #sys.argv[1],sys.argv[2],sys.argv[3]
    #m = s.get_sign()
    #print('返回text：',s.get_Iostock())
    s.json2sql()
    print('done')