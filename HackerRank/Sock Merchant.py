def sockMerchant(n,ar):
    dict = {}
    m = 0
    for key in ar:
        dict[key] = dict.get(key,0)+1
    for i in dict.values():
        m += int(i/2)
    return m




if __name__=='__main__':
    n = int(input())
    ar = list(map(int,input().rstrip().split()))
    res = sockMerchant(n,ar)
    print(res)