# WAP to count the letters in the list
l= input("Enter the words :- ")
word=''
count=0
for i in l:
    c= i.isalpha()
    if c==True:
        word+=i
        count+=1
print(count)
    