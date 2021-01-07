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
thread1.run()