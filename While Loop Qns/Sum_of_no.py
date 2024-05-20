n=int(input("Enter only 0 & 1: "))
a=0
while n!=0:
    r=n%10
    a+=r
    n=n//10
print(f'The sum of the digits are:- {a}')