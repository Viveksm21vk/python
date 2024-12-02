n = int(input())
Sum = 0
count = 1
while(count == 1 or Sum >= 10):
    if(count != 1):
        n = Sum
        Sum = 0
    while(n > 0):
        rem = n % 10
        Sum += rem
        n //= 10
    count += 1
print(Sum)