import time
def display_digits(l1):
    for i in l1:
        print(i)
        time.sleep(1)
def display_letters(l2):
    for i in l2:
        print(l2)
        time.sleep(1)

l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']
display_digits(l1)
display_digits(l2)