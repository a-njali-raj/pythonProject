dict={}
str=input("enter the string:")
x=str.split()
print(x)
for i in x:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print("character frequency is:")
for x,y in dict.items():
        print(x,y)
