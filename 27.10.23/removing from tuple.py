# Write a Python program to remove an item from a tuple.
t=(1,2,3,4,5,6,7,8,9)
l= list(t)
i= int (input("Enter the index of tuple to be removed:- "))
l.pop(i)
print(tuple(l))
