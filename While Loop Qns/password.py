pass1= "Arjit"
time=0
while time!=3:
    pass2= input("Enter the Password:- ")
    if pass1==pass2:
        print("Congratulations tou have successfully gussed the correct password")
        break
    else:
        print("Wrong Password")
        time+=1
    if time==3:
        count=0 
        print("Try again after 30 sec")