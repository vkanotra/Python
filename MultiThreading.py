from threading import *
from time import *


class Hello(Thread):
    def run(self):                                 # run is an inbuilt method of class thread
        for i in range(10):
            print("Hello")
            sleep(0.5)                                # to make it sleep for 1 sec, so we can see the output


class Hi(Thread):
    def run(self):
        for i in range(10):
            print("Hi")
            sleep(0.5)


obj1 = Hello()
obj2 = Hi()

# obj1.daemon = True                                if thread is daemon, it will stop when main thread stops
# obj2.daemon = True                                and may or may not execute fully

obj1.start()                                         # start is used to execute 'run method'
sleep(0.2)                                           # to avoid collision (HiHello)
obj2.start()


obj1.join()
obj2.join()

print("bye")
# T1 thread will run obj1, T2 will run obj2, Main Thread will run print(bye)
# to make main thread wait for T1 and T2 to complete, we use join
