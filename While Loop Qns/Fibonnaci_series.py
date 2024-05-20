'''

n= int(input())
a= 0 
b= 1
while True:
    a+=b
    a=b
    print(a)
    b+=1
    break'''

n = int(input("Enter the number of terms in the Fibonacci sequence: "))
a, b = 0, 1
count = 0
if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci sequence:")
    while count < n:
        print(a, end=" ")
        a, b = b, a + b 
        count += 1

# n= int(input())
# a=0
# b=1
# print(a,b, end=" ")
# while n-2>0:
#     c=a+b
#     print(c,end=" ")
#     a,b= b,a+c
#     n-=1