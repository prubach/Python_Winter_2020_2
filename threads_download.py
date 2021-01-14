from knotprot_download import get_proteins, setup_download_dir, download_link, time_it
from functools import partial
from multiprocessing.pool import Pool
from threading import Thread
from queue import Queue

def run_single(dir):
    proteins = get_proteins()
    for pr in proteins:
        download_link(dir, pr)


def run_parallel(dir):
    proteins = get_proteins()
    download = partial(download_link, dir)
    # 5 at a time
    with Pool(10) as pool:
        pool.map(download, proteins)


class DownloadWorker(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            dir, prot = self.queue.get()
            try:
                download_link(dir, prot)
            finally:
                self.queue.task_done()


def run_workers(dir):
    proteins = get_proteins()
    queue = Queue()
    for n in range(10):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()
    for p in proteins:
        queue.put((dir, p))
    queue.join()


#print(get_proteins())
dir = setup_download_dir()

#time_it(run_single, dir)
time_it(run_parallel, dir)
#time_it(run_workers, dir)
