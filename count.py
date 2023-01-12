n=int(input("enter the number of strings:"))
print("enter the strings:")
list=[]
count=0
for i in range (0,n):
    ele=input()
    list.append(ele)
print(list)
for i in list:
    for j in i:
        if j=="a":
            count=count+1
print(count)