n = int(input("Please enter the number of lines:"))
asc = ord('Z')
for i in range(n):
    for j in range(1,6):
        if(i==0 or j==1 or j==5 or i==n-1):
            print(chr(asc),end="")
        else:
            print(" ",end="")
    print()
    asc -= 1