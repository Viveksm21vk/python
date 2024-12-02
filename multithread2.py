import threading
import time
def display_digits(l1):
    for i in l1:
        print(i)
        time.sleep(1)
def display_letters(l2):
    for i in l2:
        print(i)
        time.sleep(1)

l1 = [1,2,3,4,5]
l2 = ['a','b','c','d','e']
thread1 = threading.Thread(target=display_digits,args=(l1,))
thread2 = threading.Thread(target=display_letters,args=(l2,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Tasks completed successfully by two threads.")