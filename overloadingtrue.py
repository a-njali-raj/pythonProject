class A:
 def __init__(self,a,b):
    self.a=a
    self.b=b
 def __add__(self,other):
    return self.a+other.a,self.b+other.b
 def __str__(self):
     return self.a,self.b
o1=A(2,4)
o2=A(5,6)
o3=A("helloo","hi")
o4=A("How are you?","well")
print(o1+o2)
print(o3+o4)

