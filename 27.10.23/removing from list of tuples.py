# Write a Python program to replace last value of tuples in a listsample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_value = 100
updated_list = [(x[0], x[1], new_value) for x in sample_list]
print(updated_list)
