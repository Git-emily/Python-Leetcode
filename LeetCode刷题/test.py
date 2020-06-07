class A:
    pass

class B(A):
    pass

print(type(A()))
print(A)
print(isinstance(A(),A))
print(type(A()) ==A)
print(isinstance(B(),A))
print(B())
print(A())