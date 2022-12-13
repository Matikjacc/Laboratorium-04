import time
import sys
import numpy as np
import matplotlib.pyplot as plt

m = 0
with open('M.txt') as f:
    m = int(f.readline())

sys.setrecursionlimit(3000)

# fib(36) 6 sek rekursywnie

def fib_iter(n):
    print(n)
    n1 = 1
    n2 = 1
    for i in range(2, n):
        temp = n2
        n2 = n1 + n2
        n1 = temp
    return n2


def fib_rec(n):
    if n == 1 or n == 2:
        return 1
    else:
        return (fib_rec(n - 1) + fib_rec(n - 2))


def fib_rec_mem(n, dictonary):
    if n in dictonary:
        return dictonary
    else:
        fib_rec_mem(n - 1, dictonary)
        dictonary[n] = dictonary[n - 1] + dictonary[n - 2]
        return dictonary

n = 0

keys_for_graph = []
table_of_time_iter = []
table_of_time_rec = []
table_of_time_rec_mem = []
start_time = 0
end_time = 0
k = 0
while end_time - start_time < 0.1 and k < m:
    start_time = time.time()

    fib_iter(k + 1)

    end_time = time.time()

    table_of_time_iter.append(end_time - start_time)
    k += 1
for i in range(len(table_of_time_iter)):
    keys_for_graph.append(i+1)
plt.bar(keys_for_graph, table_of_time_iter)
plt.xlabel("Nth fibonacci value (using iter function)")
plt.ylabel("Time to calculate it")
plt.show()

keys_for_graph = []
table_of_time_iter = []
table_of_time_rec = []
table_of_time_rec_mem = []
start_time = 0
end_time = 0
k = 0
while end_time - start_time < 0.1 and k < m:
    start_time = time.time()

    fib_rec(k + 1)

    end_time = time.time()

    table_of_time_iter.append(end_time - start_time)
    k += 1
for i in range(len(table_of_time_iter)):
    keys_for_graph.append(i+1)
plt.bar(keys_for_graph, table_of_time_iter)
plt.xlabel("Nth fibonacci value (using recursive function)")
plt.ylabel("Time to calculate it")
plt.show()

keys_for_graph = []
table_of_time_iter = []
table_of_time_rec = []
table_of_time_rec_mem = []
start_time = 0
end_time = 0
k = 0
while end_time - start_time < 0.1 and k < m:
    start_time = time.time()

    dictonary = {1: 1, 2: 1}
    dictionary = fib_rec_mem(n, dictonary)

    end_time = time.time()

    table_of_time_iter.append(end_time - start_time)
    k += 1
for i in range(len(table_of_time_iter)):
    keys_for_graph.append(i+1)
plt.bar(keys_for_graph, table_of_time_iter)
plt.xlabel("Nth fibonacci value (using recursive with memoizeiton function)")
plt.ylabel("Time to calculate it")
plt.show()

