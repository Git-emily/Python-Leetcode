import hashlib
import json
import sys
import time
from urllib import parse
import pymssql
import requests

import xlwt
wb = xlwt.Workbook()


class Port_delivery:
    def __init__(self, create_starttime,secret_key):
        self.create_starttime = create_starttime
        self.secret_key = secret_key

    def get_sign(self):
        strs = ''
        self_param = {'flag': 'Testing', 'method': 'delivery.getList',
                      'type': 'json', 'timestamp': int(time.time()),
                      'create_starttime': self.create_starttime
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

    def get_delivery(self):
        base_url = 'http://two.erp.taoex.com/index.php/openapi/rpc/service/'
        param = {'flag': 'Testing', 'sign': self.get_sign(), 'method': 'delivery.getList',
                 'type': 'json', 'timestamp': int(time.time()),
                 'create_starttime': self.create_starttime
                 }
        request_param = parse.urlencode(param).encode(encoding='utf-8')
        #print('参数是:',request_param)
        header = {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'}
        response_delivery = requests.post(base_url, data=request_param, headers=header)
        return response_delivery

        # 将表结构写入excel中
    def json2Excel(self):
        Delivery_file = self.get_delivery()
        responses = json.loads(Delivery_file.text)
        item = responses['response']['lists']
        for item3 in item:
            for item5 in item[item3]['items']:
                first = list(item[item3].keys())
                second = list(item[item3]['items'][item5].keys())
                first +=second

        ws = wb.add_sheet('data')
        print(first)
        # print(first)
        for i in range(len(first)):
            ws.write(0, i, first[i])
        wb.save('/Users/Administrator/Desktop/Data2.xls')

    def json2sql(self):
        list1 = []
        # 链接数据库
        conn = pymssql.connect('WIN-8D5O9I2ISMB', 'emily', 'Yr5258800a', 'DBSource')
        cur = conn.cursor()  # 创建游标对象，sql语句的执行基本都在游标上

        # 创建数据库表
        cur.execute(""" if not exists(select * from sysobjects a where a.name = 'STG_Delivery')
        create table STG_Delivery(
            count nvarchar(25),
            shop_code nvarchar(150),
            shop_name nvarchar(25),
            order_no  nvarchar(255),
            member_name  nvarchar(255),
            delivery_bn nvarchar(255),
            create_time nvarchar(255),
            ship_time nvarchar(255),
            freight_amount nvarchar(255),
            logi_name nvarchar(255),
            logi_no nvarchar(255),
            branch_name nvarchar(255),
            branch_bn nvarchar(25),
            delivery_no nvarchar(255),
            consignee nvarchar(255),
            consignee_area nvarchar(255),
            consignee_addr nvarchar(255),
            consignee_zip nvarchar(255),
            consignee_tel nvarchar(255),
            consignee_mobile nvarchar(25),
            consignee_email nvarchar(255),
            mark_memo nvarchar(255),
            custom_memo nvarchar(255),
            bn nvarchar(255),
            product_name nvarchar(255), 
            price nvarchar(255),
            nums nvarchar(255),
            update_time datetime)
        """)

       # 获取json文件
        Delivery_file = self.get_delivery()
        #print('response:',Delivery_file.text)
        #print('开始解析')
        responses = json.loads(Delivery_file.text)  # response为dict
        # print(type(responses))
        #print('response值:',responses)
        item1 = responses['response']
        item2 = item1['lists']
        item = responses['response']['lists']
        for item3 in item:
            for item5 in item[item3]['items']:
                '''
                if item[item3].get("order_items") == None:
                    print(item5)
                    order_items = 'NULL'
                    '''
                item6 = item[item3]['items'][item5]

                sql_value = (item1["count"],
                             item2[item3]["shop_code"],item2[item3]["shop_name"],item2[item3]["order_no"],item2[item3]["member_name"],
                             item2[item3]["delivery_bn"], item2[item3]["create_time"], item2[item3]["ship_time"],item2[item3]["freight_amount"],
                             item2[item3]["logi_name"], item2[item3]["logi_no"],  item2[item3]["branch_name"], item2[item3]["branch_bn"],item2[item3]["delivery_no"],
                             item2[item3]["consignee"], item2[item3]["consignee_area"], item2[item3]["consignee_addr"],item2[item3]["consignee_zip"],
                             item2[item3]["consignee_tel"], item2[item3]["consignee_mobile"], item2[item3]["consignee_email"],
                             item2[item3]["mark_memo"],
                             item2[item3]["custom_memo"],

                            item6['bn'],item6['product_name'],item6['price'],item6['nums'],

                             time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

                list1.append(sql_value)
        #print('list1', list1)

        # 向SQL SER插入数据
        sql = "insert into STG_Delivery values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
              "%s,%s,%s,%s,%s,%s) "
        
        cur.executemany(sql, list1)

        conn.commit()
        conn.close()


if __name__ == '__main__':
    s = Port_delivery('2019-01-01 18:12:00','egCFpcGpliNUyIDjtwjNhIJeBSWiSzYJ')  # sys.argv[1],sys.argv[2],sys.argv[3]
    #s.json2Excel()
    s.json2sql()
    print('done')

