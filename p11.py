# WAP to find the no. of currency notes of each type.
amt= int(input("Enter the amount to be withdrawn:- "))-100
twoth_amt= amt//2000
amt= amt % 2000
fiveh_amt= amt//500
amt= amt % 500
hunh_amt= amt//100

print("The no. of notes of 2000 is:- ", twoth_amt)
print("The no. of notes of 500 is:- ", fiveh_amt)
print("The no. of notes of 100 is:- ", hunh_amt+1)
