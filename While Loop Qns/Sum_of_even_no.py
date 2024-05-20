n = int(input("Enter a positive integer (n): "))
sum = 0
current_number = 2  
while current_number <= n:
    sum += current_number
    current_number += 2 
print(f"The sum of even numbers from 2 to {n} is: {sum}")
