import time
from ll_queue import LLQueue
from arr_queue import ArrQueue

n = 100000

llqq = LLQueue()
arrq = ArrQueue()

start_ime = time.time()

for i in range(n):
    llqq.enqueue(n)

end_time = time.time()

print(f'LinkedLis enqueue time: {end_time - start_ime} seconds')

start_ime = time.time()

for i in range(n):
    arrq.enqueue(i)

end_time = time.time()

print(f'ArrLink enqueue time: {end_time - start_ime} seconds')

start_ime = time.time()

for i in range(n):
    llqq.dequeue()

end_time = time.time()

print(f'LinkedList dequeue time: {end_time - start_ime} seconds')

start_ime = time.time()

for i in range(n):
    arrq.dequeue()

end_time = time.time()

print(f'ArrLink dequeue time: {end_time - start_ime} seconds')
