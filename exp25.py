colour1=input("enter the colors")
colour_list1=colour1.split(",")
print(colour_list1)
colour2=input("enter the colours")
colour_list2=colour2.split(",")
print(colour_list2)
x=(set(colour_list1).difference(colour_list2))
print(x)