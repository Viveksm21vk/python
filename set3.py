s1 = {1,2,3,4,5}
s2 = {4,5,6,7}
s3 = {1,2,3}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issuperset(s3))
print(s2.issubset(s1))
print(s3.issubset(s1))