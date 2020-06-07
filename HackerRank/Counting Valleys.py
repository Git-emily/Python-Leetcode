def countingValleys(n,s):
    s = list(s)
    s = ['-1' if x == 'D' else '1' for x in s]
    sum = 0
    l = 0
    res = 0
    for i in range(len(s)):
        sum += int(s[i])
        l +=1
        if sum == 0 and int(s[i+1-l]) < 0 :
            res += 1
            i = i-l+2
        if sum == 0:
            i = l
            l = 0
    return res

if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n,s)
    print(result)