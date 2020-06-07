import sys
n = int(input())
lines = []
dic ={}
for i in range(n):
    lines.append(input().split())
#print(lines)    #注意注意⚠️输出的值！！！！！
for item in lines:
    #print(item)
    for m in item:
        dic[m] = dic.get(m,0)+1
print(max(dic.values()))
