''''# Input the basic salary of the employee
basic_salary = float(input("Enter the basic salary of the employee: "))

# Calculate HRA and DA based on the given conditions
if basic_salary <= 10000:
    hra_percentage = 0.20
    da_percentage = 0.80
elif basic_salary <= 20000:
    hra_percentage = 0.25
    da_percentage = 0.90
else:
    hra_percentage = 0.30
    da_percentage = 0.95

# Calculate HRA, DA, and Gross Salary
hra = basic_salary * hra_percentage
da = basic_salary * da_percentage
gross_salary = basic_salary + hra + da

# Display the calculated Gross Salary
print(f"Gross Salary: {gross_salary:.2f}")
'''''
''''
n= int(input("Enter a positive integer: "))
if n%2==0:
    print(f"{n} is an even number")
else:
    print(f"{n} is an odd number")
'''''
n= int(input())
