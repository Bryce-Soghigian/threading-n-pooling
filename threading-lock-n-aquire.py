from threading import Lock,Thread
"""

Python thread locking

the threading module in python has a sync tool called lock
A lock class has two methods

_ acquire(): this method locks the lock and blocks execution until it is released
_ release(): THis method is used to release the lock. THis method is called in the locked state.
lock.acquire() is used to lock when the state is unlocked and return immediately.
lock.release() is used to unlock the state this is only called when the state is locked.
Threads.append(Thread(target=func)) used to instantiate it with a target function.
threads[-1].start() used to call start, print(a)gives the final value.



"""
lock = Lock()
a = 1
def multiply_one():
    global a
    lock.acquire()
    a*= 4
    lock.release()

def multiply_two():
    global a
    lock.acquire()
    a *= 6
    lock.release()

threads = []
for func in [multiply_one,multiply_two]:
    threads.append(Thread(target=func))
    threads[-1].start()

for thread in threads:
    thread.join()

print(a)