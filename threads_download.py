from knotprot_download import get_proteins, setup_download_dir, download_link, time_it, create_thumbnail
from functools import partial
from multiprocessing.pool import Pool
from threading import Thread
from queue import Queue
from concurrent.futures.process import ProcessPoolExecutor
from pathlib import Path

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
    for n in range(16):
        worker = DownloadWorker(queue)
        worker.daemon = True
        worker.start()
    for p in proteins:
        queue.put((dir, p))
    queue.join()


def thumbnails_single(dir):
    for image_path in Path(dir).iterdir():
        #print(image_path)
        create_thumbnail((256, 256), image_path)


def thumbnails_multi(dir):
    create_thumbs = partial(create_thumbnail, (256, 256))
    with ProcessPoolExecutor() as executor:
        executor.map(create_thumbs, Path(dir).iterdir())


#print(get_proteins())
dir = setup_download_dir()

#time_it(run_single, dir)
#time_it(run_parallel, dir)
time_it(run_workers, dir)

#time_it(thumbnails_single, 'images')
time_it(thumbnails_multi, 'images')