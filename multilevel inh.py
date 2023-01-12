class grandfather:
    def __init__(self,gfname):
        self.gfname=gfname
class father(grandfather):
    def __init__(self,fname,gfname):
        self.fname=fname
        grandfather.__init__(self,gfname)
class daughter(father):
            def __init__(self,dname,fname,gfname):
                self.dname=dname
                father.__init__(self,fname,gfname)
            def show(self):
                    print("Grand father name:",self.gfname)
                    print("Father name:",self.fname)
                    print("Daughter name:",self.dname)
d=daughter("anjali","raju","raman")
d.show()
