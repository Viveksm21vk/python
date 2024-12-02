n = int(input("Please enter number of lines:"))
Asc = 65
for i in range(n):
    for j in range(i+1):
        print(chr(Asc+j),end="")
    print()