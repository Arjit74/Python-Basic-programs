# Write a Python program to check whether an element exists within a tuple.
t=(1,2,3,4,5,6)
i= int(input())
for i in t:
    if i in t:
        print("Yes the element exist in the tuple")
    else:
        print("No the element exist in the tuple")
