class team:
    def __init__(self,name,age):
        self._name=name
        self._age=age
    def display(self):
        print("my name is:",self._name)
t=team("Anjali",21)
t.display()
print(t._age)

