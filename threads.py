import threading
import time

class MyThread(threading.Thread):
    def __init__(self, thread_name, delay, counter):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.delay = delay
        self.counter = counter

    def run(self):
        print('Starting: ' + self.thread_name)
        while self.counter > 0:    #while self.counter:
            time.sleep(self.delay)
            print('%s: %s' % (self.thread_name, time.ctime(time.time())))
            self.counter -= 1

#print(time.ctime(time.time()))

thread1 = MyThread('Thread 1', 1, 5)
thread2 = MyThread('Thread 2', 1, 5)
thread3 = MyThread('Thread 3', 1, 5)
# Sequentially
#thread1.run()
#thread2.run()

# in parallel
thread1.start()
thread2.start()
thread3.start()

#thread1.join()


all_threads = []
all_threads.append(thread1)
all_threads.append(thread2)
all_threads.append(thread3)

for thr in all_threads:
    thr.join()


print('Exiting main thread')