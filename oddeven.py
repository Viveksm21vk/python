l = [1,2,3,4,5,6,7,8,9,0]
odd_list = []
even_list = []
for i in l:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)