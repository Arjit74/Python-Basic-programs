# Write a function to calculate area and perimeter of a rectangle

def Area_Of_Rectangle(l,b):
    area = l*b
    return(area)
def Peri_Of_Rectangle(l,b):    
    peri = 2*(l+b)
    return(peri)

# main code
lenght = int(input("Enter the lenght of rectangle: "))
breadth = int(input("Enter the breadth of rectangle: "))
area = Area_Of_Rectangle(lenght,breadth)
perimeter = Peri_Of_Rectangle(lenght,breadth)
print(f'Area of the Rectangle is: {area}')
print(f'Perimeter of the Rectangle is: {perimeter}')