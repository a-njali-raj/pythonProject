class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)

class Father:
    fathername=""
    def father(self):
        print(self.fathername)

class daughter(Mother,Father):
    def parents(self):
        print("Mother:",self.mothername)
        print("father:",self.fathername)
d=daughter()
d.mothername="Ambika"
d.fathername="Raju"
d.parents()
