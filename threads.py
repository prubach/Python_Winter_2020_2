import threading
import time
import multiprocessing

class MyThread(threading.Thread):
    def __init__(self, thread_name, delay, counter, shared_list):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.delay = delay
        self.counter = counter
        self.shared_list = shared_list

    def run(self):
        print('Starting: ' + self.thread_name)
        while self.counter > 0:    #while self.counter:
            time.sleep(self.delay)
            print('%s: %s' % (self.thread_name, time.ctime(time.time())))
            self.shared_list.append(self.thread_name + ': ' + str(self.counter))
            self.counter -= 1

print('CPUs: %s' % (multiprocessing.cpu_count()))

#print(time.ctime(time.time()))

shared_list = []

thread1 = MyThread('Thread 1', 1, 10, shared_list)
thread2 = MyThread('Thread 2', 1, 10, shared_list)
thread3 = MyThread('Thread 3', 1, 10, shared_list)
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
# Thread safety !!!
print('Shared list: ' + str(shared_list))

print('Exiting main thread')