# WAP to input twp no.s and print the swapped values of them.
num1= eval(input("Enter the first number:- "))
num2= eval(input("Enter the second number:- "))
print("The original no.s are",num1,"&",num2)
num1,num2=num2,num1
print("The swapped values are:-",num1,"&",num2)
