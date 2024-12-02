import time
import threading

print("VS Code has opened.")
def coding():
    print(f"Hello from {threading.current_thread().name}")
    for i in range(5):
        print("Coding . . .")
        time.sleep(1)
def error_check():
    print(f"Hello from {threading.current_thread().name}")
    for i in range(5):
        print("Checking for errors . . .")
        time.sleep(1)
def auto_save():
    print(f"Hello from {threading.current_thread().name}")
    for i in range(5):
        print("Saving . . .")
        time.sleep(1)

t1 = threading.Thread(target=coding,name="coder")
t2 = threading.Thread(target=error_check,name="tester")
t3 = threading.Thread(target=auto_save,name="saver")
t2.daemon = True
t3.daemon = True
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("VS Code has closed.")