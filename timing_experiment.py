import time
from memory_solver import OperationGuess
from solver import solve
import random

# AVERAGE CASE
o = OperationGuess()
for i in range(10, 100, 10):
    o.reset_memory()
    lst = [random.randint(0, 10) for _ in range(i)]
    t = tuple(lst)
    print("lst size = {} target = 50".format(len(lst)))
    s = time.time()
    o.solve(t, 50)
    e = time.time()
    print("Memory Time: {}".format(e - s))

    s = time.time()
    solve(lst, 50)
    e = time.time()
    print("Regular Time: {}".format(e - s))


# WORST CASE
# o = OperationGuess()
# for i in range(3, 100):
#     o.reset_memory()
#     lst = []
#     MAX = 1
#     for _ in range(i):
#         rn = random.randint(2, 10)
#         lst.append(rn)
#         MAX *= rn
#
#     t = tuple(lst)
#     print("lst size = {} target = {}".format(len(lst), MAX))
#     s = time.time()
#     o.solve(t, MAX + 1)
#     e = time.time()
#     print("Memory Time: {}".format(e - s))
#
#     s = time.time()
#     solve(lst, MAX + 1)
#     e = time.time()
#     print("Regular Time: {}".format(e - s))
