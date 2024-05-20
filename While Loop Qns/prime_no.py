'''
num = int(input("Enter a positive integer: "))
is_prime = True
if num < 0:
    print('Please enter  a positive no.')
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
'''
n= int(input())
count=0
i=1
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print('The number is a prime number')
else:
    print('Not a prime no. ')