from collections import Counter
dic = {}
list2=[]
list1 = list(input())   #将str转化为list
N = int(input())
dic = Counter(list1)   #统计字典中元素出现个数，并按倒叙排列
#print(dic)
dic = sorted(dic.values(),reverse=True)  #对字典中值进行排序，并存在列表中
while N>0:
    dic[0]-=1
    N-=1
    dic.sort(reverse=True)
#print(dic)
print(sum([i**2 for i in dic]))

'''
#方法2（时间更短）：
for i in list2:
    if i in dic:
        dic[i] +=1
    else:
        dic[i]=1
dic = sorted (dic.values(),reverse=True)
'''

