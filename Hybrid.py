class School:

    def school(self):
        print("This is in school")
class Std1(School):
    def std1(self):
        print("This is student 1")
class Std2(School):
    def std2(self):
        print("This is student 2")
class Mca(Std1,Std2):
    def mca(self):
        print("This is in mca")
o=Mca()
o.school()
o.std1()
o.std2()
o.mca()
