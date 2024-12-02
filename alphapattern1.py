n = int(input("Enter number of lines:"))
ch = chr(64+n)
asc =ord(ch)
for i in range(n,0,-1):
    for j in range(0,i):
        print(chr(asc),end="")
    print()
    asc -= 1
