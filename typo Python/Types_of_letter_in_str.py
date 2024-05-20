# n= input()
# no= [1234567890]
# vow= "aeiouAEIOU"
# countvow=0
# countint=0
# coountcon=0
# countspace=0

# for i in n:
#     if i in no:
#         countint=+1
#         print(countint)
        
#     elif i==(vow):
#         countvow+=1
       
# print(f"Integer value has been found {countint} times")
# print(F'Vowels has been found {countvow} times')

st= input()
alp_u= 0
alp_l=0
digits=0
cons=0
vow=0
special=0
for i in st:
    if i in 'aeiouAEIOU':
            vow+=1
    elif "a"<= i <= "z":
          alp_l+=1
          cons+=1
    elif "A"<= i<="Z":
          alp_u+=1
          cons+=1
    elif "0"<=i<="9":
          digits+=1
    else:
          special+=1
          

print(f"Number of Alphabets lower case {alp_l :<30}")
print(f"Number of Digits {digits}")
print(f"Number of Consonants {cons}")
print(f"Number of Vowels {vow}")
print(f"Number of Consonants {cons}")