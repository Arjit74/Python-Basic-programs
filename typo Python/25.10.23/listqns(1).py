a=[]
while True:
    item=input("Enter the item name: ")
    if len(item)==0:
        print("The shopping list is:- ")
        break
    a.append(item)
print(a)