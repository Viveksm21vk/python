s="10 20 30 40"
l = s.split(" ")
sum = 0.0
for i in l:
    sum += int(i)
print(sum/len(l))