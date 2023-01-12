class A():
    def __init__(self):
        self.a=int(input("Enter the Element to class A:"))
class B(A):
    def __init__(self):
        A.__init__(self)
        self.b = int(input("Enter the Element to class B:"))

class C(B):
    def __init__(self):
        B.__init__(self)
        self.c = int(input("Enter the Element to class C:"))

a=C()
if ((a.a > a.b) and(a.b > a.c)):
    print("Element of Class A is Greatest:",a.a)
elif ((a.b > a.a )and (a.a > a.c)):
    print("Element of Class B is Greatest:", a.b)
else:
    print("Element of Class C is Greatest:", a.c)