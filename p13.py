# WAP to find the simple interest.
a = eval(input("Enter the principle amount:- "))
b = eval(input("Enter the rate of interest:- "))
c = eval(input("Enter the time in years:- "))
si= (a*b*c)/100
print("The amount of simple interest is:-",si)
print("The amount to be given after being mature is:-", a+si)