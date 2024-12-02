d = {'name' : 'Vivek S M', 'age':22,'course':"Electronics and Communication Engineering"}
print(d)
print(d['name'])
print(d['age'])
print(d['course'])
for i in d.keys():
    print(i)
for j in d.values():
    print(j)
for k in d.items():
    print(k)
print(d.get("name"))
print(d.pop('course'))
print(d)