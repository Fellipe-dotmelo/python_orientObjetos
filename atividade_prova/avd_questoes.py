class A:
    a = 1

class B(A):
    _c = 3

    def __init__(self):
        print(self,a)
        print(self,c)

a = A()
print(isinstance(a, B))

b = B()
print(isinstance(b, B))

b = A()
print(isinstance(b, A))
