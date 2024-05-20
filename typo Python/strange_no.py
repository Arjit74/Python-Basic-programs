n= int(input("Enter the Number: "))
st=0
for i in range (2,n):
    if n%i==0:
        flag=1
        for j in range (2,i):
            if i%j==0:
                flag=0
                break
        if flag==0:
            print("Not Strange")
            break
        st= i 
else:
    if st > n**.5:
        print("Strange")
    else:
        print("Not Strange")
