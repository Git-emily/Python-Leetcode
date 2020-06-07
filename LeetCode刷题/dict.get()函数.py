a = [1, 2, 3, 1, 1, 2]
dic = {}
for key in a:
    print(key)
    dic[key] = dic.get(key,0)+1
    #get(key, default=None),若dict中找到了key值，则返回对应值；否则返回默认值。dic中是空值，故均返回0 ，故加上1为计数
    print(dic)