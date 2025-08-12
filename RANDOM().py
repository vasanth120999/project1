# RANDOM MODULE :
# RANDOM():
"""import random
a=random.random()
print(a)"""

# RANDINT():
"""import random
a=random.randint(1,10)
print(a)"""

# CHOICE():
"""import random
a=random.choice([5,6,1,2,3])
print(a)"""

# CHOICES ():
"""import random
a=random.choices([5,6,1,2,3],k=5)
print(a)"""

# SAMPLE():
"""import random
a=random.sample([5,6,1,2,3],k=5)
print(a)"""

#GENERATE RANDOM OTP :
"""import random
otp="".join([str(random.randint(0,9)) for i in range(6)])
print(otp)"""

# DATE&TIME:
"""from datetime import datetime
a=datetime.now()
print(a)"""

# CURRENT DATE:
"""from datetime import date
a=date.today()
print(a)"""

# CURRENT TIME:
"""from datetime import datetime
a=datetime.now().time()
print(a)"""

# CONVERT A STRING TO DATE:
"""from datetime import datetime
a="2025-06-25 15:20"
c=datetime.strptime(a.%y-%m-%d %H::%M)
print(c)"""

# Get today's day of the week
"""import datetime
today = datetime.datetime.now().strftime('%A')
if today == "Saturday" or today == "Sunday":
    print("Weekend")
else:
    print("Weekday")"""

# MULTI THREADING:
"""class hello:
    def run(n):
        print(threading)
class hi:
    def run(n):
        print('hi')
t1=hello()
t2=hi()
t1.run()
t2.run()"""

"""from threading import Thread
class hello(Thread):
    def run(self):
        for i in range(12):
            print("hello")
class hi(Thread):
    def run(self):
        for i in range(12):
            print('hi')
t1=hello()
t2=hi()
t1.start()
t2.start()"""

"""from threading import Thread
from time import sleep
class hello(Thread):
    def run(self):
        for i in range(12):
            print("hello")
            sleep(1)
class hi(Thread):
    def run(self):
        for i in range(12):
            print('hi')
            sleep(1)
t1=hello()
t2=hi()
t1.start()
sleep(2)
t2.start()
t1.join()"""

# MULTI THREAD():
# CURRENT THREAD
"""import threading
import time
def demo():
    print(f"active Thread:{threading.current_thread().name}")
    time.sleep(1)
print(f"main Thread:{threading.current_thread().name}")
t1=threading.Thread(target=demo,name="worker1")
t2=threading.Thread(target=demo,name="worker2")
t1.start()
t2.start()
t1.join()
t2.join()"""

# ACTIVE COUNT:
"""import threading
import time
def demo():
    print("{Thread.active_count()}started")
    time.sleep(1)
    print("{thread.active_count()}finished")
print(f"active thread:{threading.active_count()}")
t1=threading.Thread(target=demo,name="worker1")
t2=threading.Thread(target=demo,name="worker2")
t1.start()
t2.start()
print(threading.active_count())
t1.join()
t2.join()
print(threading.active_count())"""

# MULTI PROCESSING:
"""from multiprocessing import Process
def demo():
    for i in range(5):
        print(f"numbers;{i}")
a=Process(target=demo)
a.start()
a.join()"""

# ASYNC:
import time  
"""def demo():
    print("hello")
    time.sleep(1)
    print("bye")
def main():
    for i in range(3):
        demo()
start=time.perf_counter()
main()
end=time.perf_counter()-start
print(end)
print(f"{end:0.12f}")"""



def print_diamond(n):
    # Top half
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    
    # Bottom half
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

        
def print_diamond(n):
    # Top half
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
    
    # Bottom half
    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))
print_diamond(5)
