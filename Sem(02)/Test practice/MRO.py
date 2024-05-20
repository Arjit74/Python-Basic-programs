class X:
    def speak(self):
        return "X"
    
class A():
    def speak(self):
        return "A"

class B(X):
    pass

class C(B, A):
    pass

d = C()
print(d.speak())  