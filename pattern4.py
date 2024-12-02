n = 10
count = 1
for i in range(4):
    for j in range(count):
        if j%2==0:
            print(n,end="")
            n += 10
        else:
            print("*",end="")
    count += 2
    print()
