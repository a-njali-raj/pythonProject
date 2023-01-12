dict={}
str=input("enter the string:")
for n in str:
    if n in dict:
        dict[n]+=1

    else:
        dict[n]=1
print(dict)
print("character frequency is")
for x,y in dict.items():
        print(x,y)

