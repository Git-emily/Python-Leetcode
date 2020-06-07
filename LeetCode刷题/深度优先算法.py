class D():
    def __init__(self):
        super().__init__()
        print('D')
class E():
    def __init__(self):
        #super().__init__()
        print('E')
class B(D):
    def __init__(self):
        super().__init__()
        print('B')
class C(E):
    def __init__(self):
        super().__init__()
        print('C')
class A(B, C):
    def __init__(self):
        super().__init__()
        print('A')

if __name__=='__main__':
    a = A()
    print(A.__mro__)


#结果为<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>,
# <class '__main__.C'>, <class '__main__.E'>, <class 'object'>
