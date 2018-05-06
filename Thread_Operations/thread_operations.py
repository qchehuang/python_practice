# Thread operations:

# in Python 3,thread function has been renamed as _thread

import _thread
import time

def print_time (threadName, delay):
    count = 0
    while count <= 5 :
        time.sleep(delay)
        count += 1
        print(threadName, time.ctime(time.time()))

try:
    _thread.start_new(print_time, ("thread-1", 2,))
    _thread.start_new(print_time, ("thread-2", 4,))

except:
    print("unable to start the new threads")

while 1:
    pass