list1=[1,2,4,5,6]
list2=[4,6,8,10,1]
x=len(list1)
y=len(list2)
s1=sum(list1)
s2=sum(list2)
if(x==y):
    print("list are of same length")
else:
    print("list are of different length")
if(s1==s2):
   print("sum of lists are same")
else:
    print("sum of lists are different")
print("common elements")
for i in list1:
    for j in list2:
        if(i==j):
          print(i)

