# st= input()
# l1=(list(map(str,st.split())))
# lst=[]
# for i in l1:
#     if st.istitle():
#         lst.append('True')
#         if st.istitle()==False:
#             pass
#     else:
#         lst.append('False')
# print(lst)
st = input()
l1 = list(map(str, st.split()))
lst = []

for i in l1:
    if i.istitle():  # Check if the individual word 'i' is titlecased
        lst.append('True')
    else:
        lst.append('False')

print(lst)