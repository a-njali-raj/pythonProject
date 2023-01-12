n=int(input("enter the number:"))
factorial=1
if n<0:
    print("factorial doesnot exist for negative number")
elif n==0:
    print("The factorial of 0 is 1")
else :
    for i in range(1,n+1):
        factorial=factorial*i
    print("The factorial is",factorial)
