# Write a Python program to unzip a list of tuples into individual list
l= [(1,3),(1,4),(4,5)]
lst1=[]
lst2=[]
for i,j in l:
    lst1.append(i)
    lst2.append(j)
print(lst1)
print(lst2)
