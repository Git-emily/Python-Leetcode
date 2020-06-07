# enumerate()将一个可遍历的数据对象（list、tuple、str）组合成一个索引序列，同时列出数据和数据下标，一般用在for循环中
# enumerate(sequence,[start=0]):sequence是迭代对象；strat为下边起始位置打印成
# 打印成dict
dict={}
list=[]
seasons=['one','two','three','four']
for i,item in enumerate(seasons):
    dict[item] = i
print(dict)

#类似普通的for循环
for i,item in enumerate(seasons):
    print(i,item)