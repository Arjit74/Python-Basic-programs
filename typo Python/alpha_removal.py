# Remove all Characters in a String except alphabet
st= str(input())
l=""
for i in st:
    if "a"<=i<="z" or "A"<=i<="Z":
        l+=i
        ft= f"The alphabetic characters are{l}"
        print(ft,end=",")
    # OTHER WAY
    # if st.isalpha():
    #      l+=i
    #      print(l)
