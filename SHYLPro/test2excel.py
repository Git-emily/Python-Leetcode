import os
import json
import xlwt
wb = xlwt.Workbook()

list1 = []
def json2excel():
    fp = open('/Users/Administrator/Desktop/Python/Data.json','r')
    jsdata = json.load(fp)
    print(jsdata)
    ws = wb.add_sheet('data')
    first = list(jsdata[0].keys())
    for i in range(len(first)):
        ws.write(0,i,first[i])
    for j in range(len(first)):
        m = 0
        ls = list(jsdata[j].values())
        for k in ls:
            ws.write(j+1,m,k)
            m+=1
    workbook.save('excfile.xls')
                
    '''
for k in jsdata.key():
                    if k not in list1:
                        list1.append(k)
                ws.append(list1)  #仅有标题

            with open (jsfile,'r' ,encoding = 'utf-8')as fp:
                while True:
                
                    line = fp.readline()
                    if not line:
                        break
                    jsdata = json.load(line)
                    '''

if __name__=='__main__':
    json2excel()
