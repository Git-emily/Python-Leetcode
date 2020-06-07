N=int(input())
list1 = list(map(int,input().split()))
temp = list1[:]
#print(temp)
list1.sort()
#print(list1)
coun = 0
for i in range(N):
    if list1[i]!= temp[i]:
        coun+=1
print(coun)
