from knotprot_download import get_proteins, setup_download_dir, download_link, time_it
from functools import partial
from multiprocessing.pool import Pool


def run_single(dir):
    proteins = get_proteins()
    for pr in proteins:
        download_link(dir, pr)


def run_parallel(dir):
    proteins = get_proteins()
    download = partial(download_link, dir)
    # 5 at a time
    with Pool(5) as pool:
        pool.map(download, proteins)

#print(get_proteins())
dir = setup_download_dir()

#time_it(run_single, dir)

time_it(run_parallel, dir)
