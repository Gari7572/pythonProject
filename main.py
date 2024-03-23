from multiprocessing import Process
from queue import Queue
from threading import Thread, current_thread
import time

""" Процеси """
def square(num):
    res = num * num
    print(f'Square: {res}')


def cube(num):
    res = num * num * num
    print(f'Cube: {res}')


start = time.time()

numbers = [3, 5, 7, 8, 10]
procs = []
procs2 = []

if __name__ == '__main__':
    for num in numbers:
        proc1 = Process(target=square, args=(num,))
        proc2 = Process(target=cube, args=(num,))
        procs.append(proc1)
        procs2.append(proc2)
        proc1.start()
        proc2.start()

    for proc in procs:
        proc.join()
    for proc in procs2:
        proc.join()

    finish = time.time()
    print(f'Finished in {round(finish - start, 3)} second(s)')

""" Черга """

# q = Queue()
#
#
# def pop_nitems(n):
#     for i in range(n):
#         item = q.get()
#         time.sleep(2)
#
#         print("Thread {}. Processed Item : {}".format(current_thread().name, item))
#
#
# if __name__ == "__main__":
#
#     for i in range(1, 15):
#         q.put("Task-{}".format(i))
#
#     thread1 = Thread(target=pop_nitems, args=(3,), name="Process-3Items")
#     thread2 = Thread(target=pop_nitems, args=(4,), name="Process-4Items")
#     thread3 = Thread(target=pop_nitems, args=(5,), name="Process-5Items")
#
#     thread1.start()
#     thread2.start()
#     thread3.start()
#
#     print("\nExited from Main Thread\n")
