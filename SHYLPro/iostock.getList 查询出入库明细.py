import json
import xlwt

def json2excel():
    fp_tmp = json.load(open("D:/SHYLPro/Data2.json",'r',encoding='utf-8'))
    fp = fp_tmp['response']['lists']
    print(fp)
    wb = xlwt.Workbook()
    ws=wb.add_sheet('data')
    first = list(fp[0].keys())
    for i in range(len(first)):
        ws.write(0,i,first[i])
    for j in range(0,len(fp)):
        m = 0
        list1 = list(fp[j].values())
        for k in list1:
            ws.write(j+1,m,k)
            m+=1
    wb.save('SHYL.xls')

def getUrl():
    base_url = 'http://www.xxx.com/index.php/openapi/rpc/service/'


if __name__ =='__main__':
    print(json2excel())