# Wap to remove the vowels in a given list
l= input("Enter the list:- ")
a= "aeiouAEIOU"
lst=''
for i in l:
    if i not in a:
        lst += i
print(lst)


