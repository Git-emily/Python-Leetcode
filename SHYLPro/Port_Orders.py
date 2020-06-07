import hashlib
import json
import sys
import time
from urllib import parse
import pymssql
import requests

import xlwt
wb = xlwt.Workbook()


class Port_orders:
    def __init__(self,start_time,end_time,secret_key):
        self.start_time = start_time
        self.end_time = end_time
        self.secret_key = secret_key

    def get_sign(self):
        strs = ''
        self_param = {'flag': 'Testing', 'method': 'orders.getList',
                    'type':'json','timestamp': int(time.time()),
                      'start_time': self.start_time,
                      'end_time':self.end_time
                      }
        tmp = sorted(self_param.keys())
        for i in tmp:
            strs += i + str(self_param[i])
        result = hashlib.md5(strs.encode(encoding='utf-8'))
        Res = result.hexdigest().upper()
        tmp = Res + self.secret_key
        tmp_key = hashlib.md5(tmp.encode(encoding = 'utf-8'))
        key = tmp_key.hexdigest().upper()
        #print(key)
        return key


    def get_Orders(self):
        base_url = 'http://two.erp.taoex.com/index.php/openapi/rpc/service/'
        param = {'flag': 'Testing', 'sign': self.get_sign() , 'method': 'orders.getList',
                    'type':'json','timestamp': int(time.time()),
                      'start_time': self.start_time,
                      'end_time':self.end_time
                      }
        request_param = parse.urlencode(param).encode(encoding='utf-8')
        header = {'Content-Type':'application/x-www-form-urlencoded;charset=utf-8'}
        response_orders = requests.post(base_url,data=request_param,headers=header)
        return response_orders

        # 将表结构写入excel中
    def json2Excel(self):
        orders_file = self.get_Orders()
        responses = json.loads(orders_file.text)
        ws = wb.add_sheet('data1')

        item = responses['response']['lists']
        for item3 in item:
            #for item4 in zip(item[item3]['pmts']):
            first = list(item[item3].keys())
                #second = list(item[item3]['pmts'][item4].keys())
                #third = list(item[item3]['order_items'][item5].keys())
                #first+=second

        print(first)
        for i in range(len(first)):
            ws.write(0, i, first[i])
        wb.save('/Users/Administrator/Desktop/Data3.xls')



    def json2sql(self):
        list1 = []
        # 链接数据库
        conn = pymssql.connect('WIN-8D5O9I2ISMB', 'emily', 'Yr5258800a', 'DBSource')
        cur = conn.cursor()  # 创建游标对象，sql语句的执行基本都在游标上

        # 创建数据库表
        cur.execute("""if not exists(select * from sysobjects a where a.name = 'STG_Orders')
            create table STG_Orders(
            count nvarchar(25),
            shop_code nvarchar(150),
            shop_name nvarchar(25),
            shop_type  nvarchar(255),
            order_id  nvarchar(255),
            order_bn nvarchar(255),
            process_status nvarchar(255),
            status nvarchar(255),
            pay_status nvarchar(255),
            ship_status nvarchar(255),
            shipping nvarchar(255),
            is_cod nvarchar(255),
            pay_bn nvarchar(25),
            payment nvarchar(255),
            ship_name nvarchar(255),
            ship_area nvarchar(255),
            ship_addr nvarchar(255),
            ship_zip nvarchar(255),
            ship_tel nvarchar(255),
            ship_mobile nvarchar(25),
            ship_email nvarchar(255),
            is_tax nvarchar(255),
            cost_tax nvarchar(255),
            tax_company nvarchar(255),
            currency nvarchar(255), 
            cost_item nvarchar(255),
            cost_freight nvarchar(255),
            cost_protect nvarchar(255),
            cost_payment nvarchar(255),
            discount nvarchar(255),
            pmt_goods nvarchar(25),
            pmt_order nvarchar(255),
            total_amount nvarchar(255),
            final_amount nvarchar(255),
            payed nvarchar(255),
            createway nvarchar(255),
            order_type nvarchar(255),
            last_modified nvarchar(255),
            paytime nvarchar(255),
            order_createtime nvarchar(255),
            download_time nvarchar(255),
            member_id nvarchar(25),
            member_name nvarchar(25),
            pmts_id nvarchar(255),
            pmts_order_id nvarchar(255),
            pmt_amount nvarchar(255),
            pmt_memo nvarchar(255),
            pmt_describe nvarchar(255),
            is_modify nvarchar(255),
            bn nvarchar(255),
            barcode nvarchar(255), 
            name nvarchar(255),
            nums nvarchar(255),
            sendnum nvarchar(25),
            item_type nvarchar(255),
            weight nvarchar(255),
            cost nvarchar(255),
            price nvarchar(255),
            pmt_price nvarchar(255),
            sale_price nvarchar(255),
            sales_amount nvarchar(255),
            update_time datetime
            ) """)  # 三引号的作用，将字符串原样复制

        # 获取json文件
        Orders_file = self.get_Orders()
        # print('response:',Iostock_file.text)
        # print('开始解析')
        responses = json.loads(Orders_file.text)  # response为dict
        # print(type(responses))
        #print('response值:',responses)
        item1 = responses['response']
        item2 = item1['lists']
        item = responses['response']['lists']
        for item3 in item:

            for item5 in item[item3]['order_items']:
                if item[item3].get("order_items") == None:
                    print(item5)
                    order_items = 'NULL'
                item6 = item[item3]['order_items'][item5]


                for item3 in item2:
                    if item2[item3]['pmts'] is not None:
                        for item4 in item2[item3]['pmts']:


                            sql_value = (item1["count"],
                                         item2[item3]["shop_code"],item2[item3]["shop_name"],item2[item3]["shop_type"],item2[item3]["order_id"],
                                         item2[item3]["order_bn"], item2[item3]["process_status"], item2[item3]["status"],item2[item3]["pay_status"],
                                         item2[item3]["ship_status"], item2[item3]["shipping"], item2[item3]["is_cod"],item2[item3]["pay_bn"],
                                         item2[item3]["payment"], item2[item3]["ship_name"], item2[item3]["ship_area"],item2[item3]["ship_addr"],
                                         item2[item3]["ship_zip"], item2[item3]["ship_tel"], item2[item3]["ship_mobile"],
                                         item2[item3]["ship_email"],
                                         item2[item3]["is_tax"], item2[item3]["cost_tax"], item2[item3]["tax_company"],
                                         item2[item3]["currency"],
                                         item2[item3]["cost_item"], item2[item3]["cost_freight"], item2[item3]["cost_protect"],
                                         item2[item3]["cost_payment"],
                                         item2[item3]["discount"], item2[item3]["pmt_goods"], item2[item3]["pmt_order"],
                                         item2[item3]["total_amount"],
                                         item2[item3]["final_amount"],
                                         item2[item3]["payed"], item2[item3]["createway"], item2[item3]["order_type"],
                                         item2[item3]["last_modified"],
                                         item2[item3]["paytime"], item2[item3]["order_createtime"], item2[item3]["download_time"],
                                         item2[item3]["member_id"],
                                         item2[item3]["member_name"],

                                        item4['id'],item4['order_id'],item4['pmt_amount'],item4['pmt_memo'],item4['pmt_describe'],

                                         item2[item3]["is_modify"],

                                        item6['bn'],item6['barcode'],item6['name'],item6['nums'],item6['sendnum'],item6['item_type'],
                                        item6['weight'], item6['cost'],item6['price'], item6['pmt_price'],
                                        item6['sale_price'], item6['sales_amount'],

                                         time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

                    print(sql_value)

        list1.append(sql_value)
                # print('list1', list1)

        # 向SQL SER插入数据
        sql = "insert into STG_IoStock values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
              "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) "
        cur.executemany(sql, list1)

        conn.commit()
        conn.close()


if __name__=='__main__':
    s = Port_orders('2010-01-03 00:00:00','2020-04-03 19:30:00','egCFpcGpliNUyIDjtwjNhIJeBSWiSzYJ') #sys.argv[1],sys.argv[2],sys.argv[3]
    s.json2Excel()
    #s.json2sql()
    print('done')

