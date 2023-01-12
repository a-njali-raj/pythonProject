class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
            print(self.a+self.b)
list=[]
list.append(A(2,5))
list.append(A(6,2))
list.append(A(4,8))
list.append(A(5,3))
for i in list:
    i.sum()