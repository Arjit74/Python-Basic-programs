

# st= str(input("Enter the string: "))
# st1= ""
# for x in st:
#     count=0
#     if x not in st1:
#         for a in st:
#             if a==x:
#                 count+=1
#         print(x,":",count)
#         st1 +=x

st= str(input("Enter the string: "))
reg=''
for ch in st:
    if ch not in st:
        count= st.count(ch)
        print((f"{ch}:{count}"))
    reg+=1