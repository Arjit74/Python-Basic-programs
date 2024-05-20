# WAP to find whether a triangle is scalene, isosceles,right angled or invalid when the sides of triangle are entered by  the user.
s1= eval(input("Enter the first side of the triangle:- "))  
s2= eval(input("Enter the second side of the triangle:- "))  
s3= eval(input("Enter the third side of the triangle:- "))  

from math import sqrt
if(sqrt(s1**2+s2**2==s3**2) or sqrt(s2**2+s3**2==s1**2) or sqrt(s1**2+s3**2==s2**2)):
    print("The triangle is a right angled triangle ")
elif(s1==s2 or s2==s3 or s3==s1):
    print("The  triangle is a isoceles triangle")
else:
    print("The triangle is a scalene triangle")