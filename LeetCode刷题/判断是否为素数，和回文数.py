import sys
import math

a, b = sys.stdin.readline().strip().split()
count = 0
list1 = []

for n in range(int(a), int(b), 1):
    if str(n) == str(n)[::-1]:
        list1.append(n)

print(list1)

for m in list1:
    for i in range(2, int(math.sqrt(m)) + 1):
        if m % i == 0:
            count-=1       #注意这种用法！！！！先减再加
            break
    count += 1
print(count)