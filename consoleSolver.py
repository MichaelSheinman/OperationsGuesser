"""
This module represents the completed solution of the original prompt
suggested by the prompt list.
"""

from solver import OperationGuess as StrategicSolver

print("""Given a sequence of numbers, and a target value, the program
will return an arithmetic expression in target. """)
curr_number = ""
numbers = ()
while curr_number != "q":
    curr_number = input("Enter an integer (q to exit): ")
    if curr_number == 'q':
        break
    try:
        curr_number = int(curr_number)
        numbers = numbers + (curr_number,)
    except ValueError:
        print("Invalid value, please try again")

target = int(input("Enter target value: "))

s = StrategicSolver()
expr = s.solve(numbers, target)
print("Numbers Entered: {}".format(str(numbers)))
print("Target Entered: {}".format(str(target)))
print("Solution: {}".format(expr))
