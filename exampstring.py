class A:
    def __init__(self,a):
        self.a=a

    def __gt__(self, other):
        if self.a>other.a:
            return True
        else:
            return False
o1=A(12)
o2=A(34)
if(o1>o2):
    print("First object is greater than second")
else:
    print("First object is less than second")

if(o1<o2):
    print("First object is less than second")
else:
    print("First object is greater than second")
if(o1==o2):
    print("First object is equal to second")
else:
    print("First object is not equal to second")



