lst = [1, 2, 3, 4, 5]
print(f"Original List: {lst}")
t = (1,2,3,4,5,6)

print(f"Original Tuple: {t}")
lst.append(6)
del lst[0]
print(f"Modified list: {lst}")
l1 = list(t)
l1.append(10)
t = tuple(l1)
print(f"Modified tuple: {t}")