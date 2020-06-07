'''样例：
输入：ZHANG SAN , LI SI ,  WANG WU , WANG LIU , WANG QI , ZHANG WU ,LIU WU;
输出：WANG WU , WANG LIU , WANG QI , ZHANG SAN , LI SI , ZHANG WU , LIU WU'
coding未实现两个姓出现的次数一样多（或者是同一个姓），按照原名单的顺序'''

import sys
from collections import Counter
listx = []
list1 = []
list2 = []
list_new = [] #定义一个空列表
count_set_a = {}
b=[]

for line in sys.stdin:
#py.3中input（）只能输入一行  sys.stdin按下换行键然后ctrl+d程序结束
    list_new = line.split()
    listx.extend(list_new)#每一行组成的列表合并
    for i in range(len(listx)):
        if listx[i] == '':
            listx.remove(listx[i])
print(listx)

for i in range(len(listx)):
    if  i % 2 == 0: #姓存储在list1中
        list1.append(listx[i])

    else:   #名存储在list2中
        list2.append(listx[i])
print(list1)
print (list2)
'''
dic = dict(zip(list1, list2))  #将两个列表，存储在dict中
print(dic)
'''

set_a = list(set(list1)) # 去重得到一个集合,但是会自动排序
print("set_a: " + str(set_a) + '\n')
set_a.sort(key = list1.index)   #按照原list1 的顺序排序
print('set_a new:' , str(set_a))

for item in set_a:
    #print('item:' , item)
    count_set_a[item]=list1.count(item)
print('count_set_a:' , str(count_set_a))
for key in list(count_set_a.keys()): #dict在遍历时不能删除，故将dict转为list进行处理
    #print('key值：', key)
    a = max(count_set_a, key=count_set_a.get)
    print(a)
    #print(count_set_a[key])
    for key1 in range(len(listx)):
        #print(listx[key1])
        if listx[key1] == a:
            b.append(listx[key1])
            print('b1:', b)
            b.append(listx[key1+1])
            print('b2' ,b)
    del count_set_a[a]   #删除最大的value对应的key值
    print('new:', count_set_a)
print('b是：', b)
for i in range(0,len(b),2):
    print(b[i] + ' ' + b[i + 1])
    '''
    if i%2==0:
        print(b[i] + ' ' + b[i+1]) '''
'''        
print(a)
sorted_count_set_a = sorted(count_set_a.items(), reverse=True)
print(sorted_count_set_a)

set_a = list(set(list1x))
#set_list1 = list(set(list1))
print(str(set_a))



m = Counter(list1)
print(m[0])

list1 = sorted(list,reverse=True)
print(list1)
#m = dict([(a.split()[1].strip(),a.split()[0].strip()) for a in list])
#print(m)
'''