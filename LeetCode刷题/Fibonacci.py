'''递归，尾递归和循环.....
计算Fibonacci数：
F(0)=F(1)=1
F(n)=F(n-2)+F(n-1),n>=2'''

'''法1：递归实现：每次求值，会把前面所有的值计算一遍，n越大，效率越低；每次递归，都会重新创建栈，n较大时也易爆栈'''
def Fibonacci1(n):
    if n < 2:
        return 1
    return Fibonacci1(n-2)+Fibonacci1(n-1)

'''法2：尾递归，效率较高'''
def Fibonacci2(n,a,b):
    if n < 2:
        return a
    else:
        return Fibonacci2(n-1,b,a+b)

'''循环，效率最高'''
def Fibonacci3(n):
    a=0
    b=1
    if n < 2:
        return b

    for i in range(1,n):
        c = a+b
        a = b
        b = c
    return c

if __name__== '__main__':
    for i in range(20):
        print(Fibonacci1(i))

    for i in range(1,21):
        print(Fibonacci2(i,1,1))

    for i in range(1,21):
        print(Fibonacci3(i))