class myclass:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sum(self):
        print(self.x+self.y)
    def sub(self):
        print(self.x-self.y)
    def mul(self):
        print(self.x*self.y)
    def div(self):
            print(self.x / self.y)

p=myclass(15,5)

p.sum()
p.sub()
p.mul()
p.div()

print(myclass)