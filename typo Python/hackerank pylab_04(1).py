# n= int(input())
# n1= int(input())
# for i in range (2,n+2):
#     if i%2==0:
#         print("1",end=" ")
#     else:
#         print("0",end=" ")

n= (input())
n1= (input())
ele= n1.split()
l=[]
for i in ele:
    if int(i)%2==0:
        l.append("1")
    else:
        l.append("0")
print(" ".join(l))