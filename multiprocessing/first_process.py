from multiprocessing import Process, set_start_method, cpu_count
from threading import Thread
from time import time

# import multiprocessing
# print(multiprocessing.cpu_count())

print("Number of processors: ", cpu_count())

def do_work():
  print("Doing work")
  i = 0
  for _ in range(10_000_000):
    i += 1
  print("Finished work")

# t1 = time()
# for _ in range(5):
#   do_work()
# t2 = time()
# print("Time taken in seconds -", t2 - t1)

def process_test():
  processes = []
  start = time()
  set_start_method("spawn")
  for _ in range(5):
    # process: separate memory space, resource heavy, isolated
    p = Process(target=do_work)
    p.start()
    processes.append(p)

  for process in processes:
    process.join()
  end = time()
  print("Time taken in seconds -", end - start)

def thread_test():
  threads = []
  start = time()
  for _ in range(5):
    # thread: shared memory space, lightweight, not isolated
    t = Thread(target=do_work)
    t.start()
    threads.append(t)

  for thread in threads:
    thread.join()
  end = time()
  print("Time taken in seconds -", end - start)


if __name__ == "__main__":
  thread_test()
