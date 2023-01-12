import csv
c_col=['ID','Name','Age']
dict_data=[{'ID':1,'Name':'Anjali','Age':18},
           {'ID':2,'Name':'Abina','Age':22},
           {'ID':3,'Name':'Anagha','Age':38},
           {'ID':4,'Name':'Ann','Age':20},
           {'ID':5,'Name':'Anitta','Age':24},
           {'ID':6,'Name':'Ameena','Age':23},
           {'ID':7,'Name':'Remya','Age':26},
           {'ID':8,'Name':'Simi','Age':27},
           {'ID':9,'Name':'Amitha','Age':29},
           {'ID':10,'Name':'Ashna','Age':30}]
try:
    with open("name.csv","w")as f:
        write=csv.DictWriter(f,fieldnames=c_col)
        write.writeheader()
        for i in dict_data:
            write.writerow(i)

except IOError:
    print("Input/Output Error")
d=csv.DictReader(open("name.csv"))
print("CSV file output is:")
for i in d:
        print(i)
