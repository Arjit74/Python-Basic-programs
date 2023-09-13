# WAP to find the hypotenuse of a right triangle.
import math
hei= eval(input("Enter the height of triangle:- "))
bas= eval(input("Enter the base of triangle:- "))
hypo= math.sqrt(hei**2 + bas**2)
print("The length of the hypotenuse is:-",hypo)
