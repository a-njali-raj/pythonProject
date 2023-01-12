x=int(input("Enter the first number:"))
y=int(input("Enter the second number"))
z=int(input("enter the third number"))
if((x>y)and(x>z)):
    largest=x
elif(y>z):
    largest=y
else:
    largest=z
    print("largest number is",largest)