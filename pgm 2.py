class Publisher:
    def __init__(self,pubname):
        self.pubname=pubname
    def display(self):
        print("Publisher :",self.pubname)

class Book(Publisher):
    def __init__(self,pubname):
        Publisher.__init__(self,pubname)
    def bookdetails(self):
        self.title=input("Book name:")
        self.author=input("Book author:")
    def display(self):
        print("Title:",self.title)
        print("Author:",self.author)
class Python(Book):
    def __init__(self,pubname):
        Book.__init__(self,pubname)
    def moredetails(self):
        self.__price=int(input("Book price:"))
        self.__pages = int(input("Book pages:"))
    def display(self):
        print("Publisher:",self.pubname)
        print("Title:",self.title)
        print("Author:",self.author)
        print("Price:",self.__price)
        print("Pages:",self.__pages)
obj=Python("DC Books")
obj.bookdetails()
obj.moredetails()
print("-------------")
obj.display()