
#x,y = input().split()
list1 = list(map(int,input().split()))
list2 = list(map(int, input().split()))
for i in range(len(list1)):    #！！！！！对list采用remove时，一定要注意，当删除元素时，数组长度会发生变化，故需要加上这句，使得对list1重新遍历
    for j in list1:
        if j in list2:
            list1.remove(j)
            list2.remove(j)
print(sorted(list1+list2))