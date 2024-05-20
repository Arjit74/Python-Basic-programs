#WAP to check whether a given string is anagram
array1= eval(input())
array2= eval(input())
lst=[]
count=0
for i in array1:
    for j in array2:
        if sorted(i)==sorted(j):
           lst.append(i,j)
print(lst)

