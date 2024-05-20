#Wap where user will enter the time in seconds display the given time in minutes,hours and seconds 
seconds = int(input("Enter time in seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(remaining_seconds).zfill(2)}")
