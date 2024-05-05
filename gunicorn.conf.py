import multiprocessing

bind = "[::]"
workers = multiprocessing.cpu_count() * 2 + 1
