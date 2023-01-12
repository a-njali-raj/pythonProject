class bank:
    def __init__(self,accn,name,accty):
        self.accn=accn
        self.name=name
        self.accty=accty
        self.bal=0

    def showamnt(self):
        print("Account holder name:",self.name)
        print("Account Number:",self.accn)
        print("Account type:",self.accty)
        print("Your balance amount:",self.bal)

    def dep(self,d1):
        self.bal=self.bal+d1
        return self.bal

    def withd(self,w1):
        self.bal=self.bal-w1
        return self.bal
n=input("Enter your name:")
a=int(input("Enter your Account number:"))
t=input("Enter your Account type:")
o=bank(a,n,t)
o.showamnt()
while(True):
    print("\nMenu")
    print("\n1.Deposit")
    print("\n2.withdraw")
    c=int(input("Enter your choice:"))
    #d=0
    if(c==1):
        d=int(input("Enter the amount to deposit:"))
        print("your total balance amount is:",o.dep(d))
    elif(c==2):
        w=int(input("Enter the amount to be withdrawn:"))
        if(w>d):
            print("Insufficient balance")
        else:
            print("Your total balance is :",o.withd(w))
    else:
        print("Enter a valid choice.")




