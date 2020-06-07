from collections import Counter
import numpy
count_dict = {}
A=[]

T = int(input())
n= int (input())
num = [int(n) for n in input().split() ]

class func():
    def get_count(self,num):
        count = Counter(num)
        count_dict = dict(count)
        #print(count_dict)
        items=sorted(count_dict.values(),reverse=True)
        #print(items)
        a=sum(items[1:])
        b=items[0]
        #print (a,b)
        if b>a:
            print('no')
        else:
            print('yes')
        '''
        #arr= numpy.array(items)   #将list转为array
        #print(arr)
        for i in range(len(items)):   
            temp = items[i]

            print(temp)
'''
        '''
        #print(items)
        backitems = [[v[1], v[0]] for v in items]
        #print(backitems)
        backitems.sort()
        return [backitems[i][1] for i in range(0, len(backitems))]
        print(backitems[i][1])
'''
if __name__ =="__main__":
    one= func()
    one.get_count(num)
