class team:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("my name is:",self.name)
t=team("Anjali",21)
t.display()
print(t.age)

