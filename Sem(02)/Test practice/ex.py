class A:
    def foo(self):
        print("A's foo")

class B:
    def foo(self):
        pass

class C(A):
    pass

class D(B, C):
    pass

d = D()
d.foo()
