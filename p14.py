# WAP to find the compound interest compounded annually.
a = eval(input("Enter the principle amount:- "))
b = eval(input("Enter the rate of interest:- "))
b1= b/100
c = eval(input("Enter the time in years:- "))
d=1 # since the interest is calculated annually 
amt= round(a*(1+(b1/d))**(d*c) , 1)
mature_amt= round(a + amt , 1 )
print("The compound interest is",amt,"and the mature amount is",mature_amt)