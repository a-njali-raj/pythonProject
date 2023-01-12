class team:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def display(self):
        print("my name is:",self.__name)
t=team("Anjali",21)
t.display()
print(t.__age)

