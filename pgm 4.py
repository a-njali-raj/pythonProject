class A():
    def __init__(self):
        self.n1=int(input("Enter the Number 1:"))
class B(A):
    def __init__(self):
        A.__init__(self)
        self.n2=int(input("Enter the Number 2:"))
class C():
    def __init__(self):
        self.n3=int(input("Enter the Number 3:"))
class D(B,C):
    def __init__(self):
        B.__init__(self)
        C.__init__(self)
        if self.n1 > self.n2 and self.n1 > self.n3:
            print("Greatest Element is in A:",self.n1)
        elif self.n2 > self.n1 and self.n2 > self.n3:
            print("Greatest Element is in B:",self.n2)
        else:
            print("Greatest Element is in C:", self.n3)

obj1=D()