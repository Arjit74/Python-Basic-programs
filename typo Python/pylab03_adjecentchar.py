'''n= str(input())
l= len(n)
if l%2==0:
    a=n[::-1]+n[2:]
    print(a)
else:
    print("Odd length.")
    '''''

st = input()
if len(st) % 2 == 0:
    swst = ""

    for i in range(0, len(st),2):
        swst += st[i+1] + st[i]

    print(swst)
else:
    print("Odd length.")
