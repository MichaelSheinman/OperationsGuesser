import timeit
from memory_solver import solve as memory_solve
from solver import solve
import random

for i in range(10, 40, 5):
    lst = [random.randint(0, 10) for _ in range(i)]
    print("lst = {} target = 50".format(lst))
    print("Memory time")
    print(timeit.timeit(memory_solve(lst, 50)))
    print("Regular time")
    print(timeit.timeit(solve(lst, 50)))
