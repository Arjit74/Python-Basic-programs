'''''
n = int(input("Enter an integer: "))
if n <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Counting down from {n} to 1:")
    
    while n >= 1:
        print(n)
        n -= 1
'''''