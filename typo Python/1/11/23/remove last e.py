# Wap for removing the last e from the list and count the remaining alphabets
phrase= input("Enter the phrase:- ")
val=0
l=[]
for i in range(len(phrase)):
    x=phrase.find("e",val)
    if x!=-1:
        l.append(x)
    val= x+1
    
print(l)
# phrase = input("Enter the phrase: ")
# val = 0
# positions = []
# while val < len(phrase):
#     index = phrase.find("e", val)
#     if index == -1:
#         break
#     positions.append(index)
#     val = index + 1

# print(positions)
