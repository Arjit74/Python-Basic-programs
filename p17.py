# WAP to input the number of heads and feets in a farm and identify the number of chickens and goats in the farm.
a= int(input("Enter the number of head:- "))
b= int(input("Enter the number of legs:- "))
c= b//4
print ("The number of goats are:-",c)
c1= b%4
c2= c1//2
print ("The number of chickens are:-",c2)
