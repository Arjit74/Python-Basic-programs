# WAP to input the number of rectangular tiles required to cover a rectangular floor.
a = int(input("Enter the length of the tile:- "))
b = int(input("Enter the breadth of the tile:- "))
c = int(input("Enter the length of the room :- "))
d = int(input("Enter the breadth of the room:- "))
ar1= a*b
ar2= d*c
arf= int(ar2/ar1)
print("The number of tiles required is:-",arf)