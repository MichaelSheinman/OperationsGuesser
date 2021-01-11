import time
from memory_solver import OperationGuess
from solver import solve
import random

o = OperationGuess()
for i in range(10, 100, 10):
    o.reset_memory()
    lst = [random.randint(0, 10) for _ in range(i)]
    t = tuple(lst)
    print("lst = {} target = 50".format(lst))
    s = time.time()
    o.solve(t, 50)
    e = time.time()
    print("Memory Time: {}".format(e - s))

    s = time.time()
    solve(lst, 50)
    e = time.time()
    print("Regular Time: {}".format(e - s))

