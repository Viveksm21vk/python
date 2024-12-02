s1 = {1,2,3,4,5}
s2 = {4,5}
s3 = {7,8,9}
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))
print(s1.issuperset(s2))
print(s2.issubset(s1))
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))