# 姓名排序
# 输入
stopword = ''
str = []
i = input()
while i != stopword:
    str.append(i)
    i = input()
print ('str是：', str )   #一维数组

# 提取姓氏
for j in range(len(str)):
    str[j]=str[j].split()    #转为二位数组；注:二维数组的创建方式，见Two-dimensional.py
print ('str is： ', str)
str2 = []
for j in range(len(str)):
    str2.append(str[j])
print('str2是： ' , str2)
# 以字典形式统计姓氏
dict = {}
for j in range(len(str)):
    if str[j][0] not in dict:   
        dict[str[j][0]] = 1  #将姓氏的数量以字典的姓氏储存起来
        #print(str[j][0])
        #print(dict)
    else:
        dict[str[j][0]] += 1

print (len(dict))

# 姓氏排序
str3 = []
for k in sorted(dict,key=dict.__getitem__,reverse=True):
    str3.append(k)
print ('str3是：', str3)
# 排序
str4 = []

for a in str3:
    for j in range(len(str)):
        if str[j][0] == a:
            str4.append(str[j][:])

print('str4: ', str4)

# 输出
for j in range (len(str)):
    for a in range(2):
        print(str4[j][a],end=' ')
    print('')