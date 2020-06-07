pre = input()
n = int(input())
words = []
for i in range(n):
    words.append(input())
print(words)
words.sort()
print(words)
for item in words:
    #print(item)
    if item[0] ==pre:
        print(item)
