import sys
team=[]
try:
    while True:
        names = sys.stdin.readline().strip()
        if names == "":
            break
    #l= list(map(str, names.split()))
    #print(names)
        item = names.split()
        #item = [int(i) for i in item]
        list.append([str(item[0],str(item[1]))])
    #b = [str(n) for n in names.split('\n')]
        #print(list)
except:
    print('wrong')
print(list)
