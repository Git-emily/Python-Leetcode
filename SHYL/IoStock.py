import pymssql
import json
import sys

list1 = []


class json2sql:
    def me_json2sql(self, file_path):
        # 链接数据库
        conn = pymssql.connect('WIN-8D5O9I2ISMB', 'emily', '5258800a@', 'DBSource')
        cur = conn.cursor()  # 创建游标对象，sql语句的执行基本都在游标上

        # 创建数据库表
        cur.execute("""
        if not exists (select * from sysobjects a where a.name='IoStock')
        create table IoStock (
            count nchar(25),
            iostock_price_num nchar(25),
            unit_cost_num nchar(25),
            iostock_id nchar(255),
            iostock_bn nchar(255),
            branch_bn nchar(255),
            branch_name nchar(255),
            bn nchar(255),
            name nchar(255),
            barcode nchar(255),
            nums nchar(255),
            type nchar(255),
            iostock_time nchar(255),
            memo nchar(255),
            original_bn nchar(255),
            iostock_price nchar(255),
            unit_cost nchar(255),
            appropriation_no nchar(255)
            ) """)  # 三引号的作用，将字符串原样复制

        # 打开json文件
        json_file = open(file_path, 'r', encoding='utf-8')
        tmp_file = json.load(json_file)["response"]  # 加载需要的字段
        print('tmp_file:', tmp_file)

        for j in tmp_file['lists']:
            sql_value = ( tmp_file["count"],tmp_file["iostock_price_num"],tmp_file["unit_cost_num"],
                j["iostock_id"], j["iostock_bn"], j["branch_bn"], j["branch_name"],
                j["bn"], j["name"], j["barcode"], j["nums"], j["type"], j["iostock_time"],
                j["memo"], j["original_bn"], j["iostock_price"], j["unit_cost"], j["appropriation_no"])
            list1.append(sql_value)
        print('list1', list1)
        try:
            cur.execute("""truncate table IoStock""")
            sql = "insert into IoStock values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.executemany(sql, list1)

        except:
            print('wrong')

        conn.commit()
        conn.close()
  # (count,iostock_price_num,unit_cost_num,iostock_id,iostock_bn,branch_bn,branch_name,bn,name,barcode,nums,type,iostock_time,memo,original_bn,iostock_price,unit_cost,appropriation_no)


if __name__ == '__main__':
    s = json2sql()
    s.me_json2sql('C:/Users/Administrator/PycharmProjects/SHYLPro/Data2.json')
