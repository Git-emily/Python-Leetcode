# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:33:24 2019

@author: PC2014101864
"""

import requests,json,pymssql,math

def login():
    url="http://api.wintalent.cn/wt/api/2.0/getToken?c=rrd"
    headers={'Content-Type':'application/json;charset=UTF-8'}
    request_param={
        "userName": "rrd",
         "password": "vSBzu7gbr8P7RANi"
    }
    response=requests.post(url,data=json.dumps(request_param), headers=headers)
    return response.json()["data"]["token"]
#    print(response.text)
#    print(response.json()["data"]["token"])
print(login())



#采集岗位信息的接口信息
def get_position(page):
    url="http://api.wintalent.cn/wt/api/2.0/auth/getPostInfo/getPositionsInfo?c=rrd&t="+login()
    headers={'Content-Type':'application/json;charset=UTF-8'}
    request_param={
          "currentPage":page,
          "customModules":"orgNameCh,recruiterUserName,recruiterRealName",
          "customFields":"100401",
          "rowSize":1000
    }
    position_response=requests.post(url,data=json.dumps(request_param), headers=headers)
    return position_response

#print(get_position(1).json()["data"])
    
#print(position_response.text)
#print(response.json()["data"])


def position_data_insert(response):
    conn = pymssql.connect("localhost", "sa", "123456", "test")
    cursor = conn.cursor()
    temp = []
    for d in response.json()["data"]:
        if d.get("recruiterRealName") == None:
            recruiterRealName='NULL'
        else:
            recruiterRealName = d.get("recruiterRealName")
        if d.get("jobLevel") == None:
            jobLevel='NULL'
        else:
            jobLevel = d.get("jobLevel")
        if d.get("endDate") == None:
            endDate='NULL'
        else:
            endDate =d.get("endDate")
        if d.get("recruitNum") == None:
            recruitNum='NULL'
        else:
            recruitNum = d.get("recruitNum")
        if d.get("projectId") == None:
            projectId='NULL'
        else:
            projectId = d.get("projectId")
        if d.get("key100401") == None:
            key100401='NULL'
        else:
            key100401 = d.get("key100401")
        position_value = (recruiterRealName,d.get("externalNameCH"),d.get("orgNameCh"),endDate,d.get("postType"),
                          d.get("addUser"),d.get("lastEditDate"),d.get("postStatus"),d.get("recruiter"),d.get("publishDate"),
                          d.get("postId"),d.get("addDate"),d.get("orgId"),jobLevel,d.get("firstPublishDate"),d.get("recruiterUserName"),
                          d.get("postCode"),recruitNum,d.get("postNameCh"),d.get("justification"),projectId,key100401)
        temp.append(position_value)
#        else:
#            print("Position error data!!!!!!")
#            print(d)
    cursor.executemany("insert into Position_new values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",temp)
    conn.commit()
    conn.close()
    
    
    

#采集日志信息的接口信息
def get_log(page,rowsize):
    url="http://api.wintalent.cn/wt/api/2.0/auth/getLogInfo/candiLogInfo?c=rrd&t="+login()
    headers={'Content-Type':'application/json;charset=UTF-8'}
    request_param={
          "currentPage":page,
          "rowSize":rowsize,
          "beginTime":"2019-05-27 00:00:00 ",
          "endTime":"2019-05-30 00:00:00 ",
          "fType":"1,2,4,5,7,9,10,11,13",
           "customFields":"persCode,pserName,channleType,oprUserName,hasRead"
    }
    log_response=requests.post(url,data=json.dumps(request_param), headers=headers)
    return log_response
#print(get_log(1).text)
#print([d["pageCount"] for d in log_response.json()["data"]][0])


    
def log_data_insert(response):
    conn = pymssql.connect("localhost", "sa", "123456", "test")
    cursor = conn.cursor()
    temp = []
    for d in response.json()["data"]:
    #    print(d)
        for item in d['rowList']:
                log_value = (d["rowSize"],d["currentPage"],d["rowCount"],d["pageCount"],
                     item['applyID'],
                     item.get("channleType"),item.get("id"),
                     item.get("ipAdd"),item.get("msg"),item.get("oprDate"),
                     item.get("oprUser"),item.get("oprUserName"),item.get("oprUserRealName"),
                     item.get("personID"),item.get("personName"),item.get("positionID"),
                     item.get("resumeID"),item.get("type"))
                temp.append(log_value)
    cursor.executemany("insert into log_new values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%"
                       "s,%s,%s,%s)",temp)
    conn.commit()
    conn.close()




log_page = [d["pageCount"] for d in get_log(1,100).json()["data"]][0]
rowCount = [d["rowCount"] for d in get_log(1,100).json()["data"]][0]


n=1
while n<math.ceil(rowCount/1000):
    log_data_insert(get_log(n,1000))
    n = n + 1
log_data_insert(get_log(math.ceil(rowCount/1000),rowCount-(math.ceil(rowCount/1000)-1)*1000))

#循环采集岗位信息，while中的条件可以按需修改
'''
i = 1
while i <=10:
    try:
        position_data_insert(get_position(i))
        i = i + 1
    except KeyError:
        break


log_page = [d["pageCount"] for d in get_log(1).json()["data"]][0]
n = 1
while n <= log_page:
    log_data_insert(get_log(n))
    n = n + 1
'''


#log_data_insert(log_response)
#position_data_insert(position_response)


#    print(d['rowList'])
#    for item in d['rowList']:
#        print(item['id'])
#for item in Asin:print (item['Asin'])
#position_data_insert(position_response)




