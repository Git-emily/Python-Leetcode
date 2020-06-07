from urllib import request
import cursor
import pymssql
import json

#加密算法
def get_MD5():
    pass

#接口连接
def get_Iostack():
    base_url = 'http://www.xxx.com/index.php/openapi/rpc/service/'
    key = 'C86732F85599E09D76A6BF45F18D5328' #将key按照加密算法来写；将method的值放在list中，循环
    url = base_url + "flag/test"+"/sign/%s"%(key)+"/method/iostock.getList"+"/type/json"
    +"/charset/utf-8"+"/ver/1/"+"/start_time/2012-11-11/end_time/2012-11-12/page_no/1/page_size/100"
    header = {'content-Type':'application/json; charset=utf-8'}
    requests_param={"start_time":"2012-12-08 00:00：00","end_time":"2012-12-09 00:00：00",
                    "branch_bn":"bianhao","page_no":"1","page_size":"100"}
    dates = json.dumps(requests_param)  #将python对象编译成json字符串
    response_iostack = request.post(url,data=dates,headers = header)  #post请求
    return response_iostack

def json2Sql(response_iostack):
    #连接数据库
    conn = pymssql.connect('WIN-8D5O9I2ISMB','emily','5258800a@','DBSource')
    curs = conn.cursor()
    list1 = []
    for temp in response_iostack.json()['response']['lists']:
        value = (temp['iostock_id'],temp['iostock_bn'])



