filename = '非结构化数据.txt'
with open(filename) as fn:
    line = fn.readline()  #初始化定义
    line_count = 1
    while line:
        print('Line{}:{}'.format(line_count , line.strip())) #strio()默认为移除字符串头尾的空格
        line = fn.readline()
        line_count +=1

from collections import Counter
with open(filename) as f:
    p = Counter(f.read().split())
    print(p)