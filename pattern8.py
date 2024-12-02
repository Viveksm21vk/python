n=int(input("Please enter number of lines: "))
for i in range(n,0,-1):
    for j in range(n-i):
        print("  ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()