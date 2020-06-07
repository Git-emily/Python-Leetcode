import pymssql
import json
import sys


class Sales:
    def me_sales(self, filename):
        conn = pymssql.connect('WIN-8D5O9I2ISMB', 'emily', '5258800a@', 'DBsource')
        cur = conn.cursor()

        cur.execute("""
            if not exists (select * from sysobjects a where a.name='Sales')
            create table Sales(
            count nchar(255),
            shop_code nchar(255),
            shop_name nchar(255),
            order_no nchar(255),
            member_name nchar(255),
            sale_no nchar(255),
            bn nchar(255),
            name nchar(255),
            spec_name nchar(25),
            price nchar(125)
            )""")

        sales_file = open(filename, 'r', encoding='utf-8')
        temp_sales = json.load(sales_file)['response']
        # print(type(temp_sales))
        # print(temp_sales)

        list1 = []
        count = temp_sales['count']
        n = temp_sales['lists']
        print('n:',n)
        for a in n:
            print('a:',a)
            # print('n[a]',n[a])
            # val1 = (n[a]['shop_code'],n[a]['shop_name'],n[a]['order_no'],n[a]['member_name'],n[a]['sale_no'])
            # tmp.append(val1)
            for d in n['1355932064461265']['sale_items']:
                # print('m[d]:',m[d])
                val = (
                    count, n[a]['shop_code'], n[a]['shop_name'], n[a]['order_no'], n[a]['member_name'], n[a]['sale_no'],
                    n['1355932064461265']['sale_items'][d]['bn'], n['1355932064461265']['sale_items'][d]['name'],
                    n['1355932064461265']['sale_items'][d]['spec_name'],
                    n['1355932064461265']['sale_items'][d]['price'])
                list1.append(val)
        print(list1)
        print(type(list1))
        cur.execute("""truncate table Sales""")
        sql = "insert into Sales values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.executemany(sql , list1)
        # (count,shop_code,shop_name,order_no,member_name,sale_no,bn,name,spec_name,pric)
        conn.commit()
        conn.close()


if __name__ == '__main__':
    s = Sales()
    s.me_sales('C:/Users/Administrator/PycharmProjects/SHYLPro/Sales.json')  #'C:/Users/Administrator/PycharmProjects/SHYLPro/Sales.json'
