from typing import Optional

IMPOSSIBLE = "Impossible"


class OperationGuess:

    def __init__(self):
        self.sequence_to_target = {}
        # sequence: {target: result}

    def reset_memory(self):
        self.sequence_to_target.clear()

    def upper_bound(self, numbers: tuple) -> int:
        """
        Generate an upper bound for the operations
        made with numbers
        >>> o = OperationGuess()
        >>> o.upper_bound((1, 3, 6)) >= 24
        True
        """
        prod = 1
        for number in numbers:
            prod *= abs(number) + 1
        return prod

    def solve2digits(self, numbers: tuple, target: int) -> str:
        """Verify whether a list of 2 numbers can be made
        equal to target.
        Precondition: numbers is a list of two integers
        Postcondition: Returns either a mathematical expression containing
        both integers that equals target, or IMPOSSIBLE if no such
        expression exists.
        >>> o = OperationGuess()
        >>> o.solve2digits((0, 1), 0)
        '0 * 1'
        >>> o.solve2digits((8, 2), 4)
        '8 / 2'
        >>> o.solve2digits((8, 2), 99)
        'Impossible'
        """
        number1 = numbers[0]
        number2 = numbers[1]

        number_tuple = tuple(numbers)
        if number1 + number2 == target:
            s = "{} + {}".format(number1, number2)
            self.add_to_memory(number_tuple, target, s)
            return s
        if number1 - number2 == target:
            s = "{} - {}".format(number1, number2)
            self.add_to_memory(number_tuple, target, s)
            return s
        if number2 - number1 == target:
            s = "{} - {}".format(number2, number1)
            self.add_to_memory(number_tuple, target, s)
            return s
        if number1 * number2 == target:
            s = "{} * {}".format(number1, number2)
            self.add_to_memory(number_tuple, target, s)
            return s
        if number2 != 0:
            if number1 / number2 == target:
                s = "{} / {}".format(number1, number2)
                self.add_to_memory(number_tuple, target, s)
                return s
        return IMPOSSIBLE

    def add_to_memory(self, sequence: tuple, target: int, s: str) -> None:
        """
        Add <target> and <s> to memory.
        """
        if sequence in self.sequence_to_target:
            self.sequence_to_target[sequence][target] = s
        else:
            self.sequence_to_target[sequence] = {}
            self.sequence_to_target[sequence][target] = s

    def check_memory(self, sequence: tuple, target: int) -> Optional[str]:
        """
        Check whether memory has <sequence> and <target>
        """
        if sequence in self.sequence_to_target:
            if target in self.sequence_to_target[sequence]:
                return self.sequence_to_target[sequence][target]
        else:
            return None

    # TODO solving algorithm may have to be updated after optimization
    def solve(self, numbers: tuple, target: int) -> str:
        """
        Solving Algorithm:
        Take two digits at a time, compute their result.
        Then see if the rest of the numbers can get to
        those two digits.
        Precondition: numbers is a list of integers
        Postcondition: Returns either a mathematical expression containing
        all the integers in number equalling target, or IMPOSSIBLE, if no
        such expression exists.
        >>> o = OperationGuess()
        >>> o.solve((1, 7, 5, 2), 9)
        '(5 - 2) - (1 - 7)'
        >>> o.solve((1, 7, 5, 2), 999)
        'Impossible'
        """

        # Manually check possibilities for list of length 0, 1, and 2
        if len(numbers) == 0:
            return IMPOSSIBLE
        if len(numbers) == 1:
            if numbers[0] == target:
                return "{}".format(numbers[0])
            else:
                return IMPOSSIBLE
        if len(numbers) == 2:
            return self.solve2digits(numbers, target)

        ub = self.upper_bound(numbers)
        lb = -ub
        if target > ub:
            return 'Impossible'
        if target < lb:
            return 'Impossible'

        memory_status = self.check_memory(numbers, target)
        if memory_status:
            return memory_status

        for i in range(len(numbers)):

            for j in range(i+1, len(numbers)):
                memory_status = self.check_memory(numbers, target)
                if memory_status:
                    return memory_status

                n1 = numbers[i]
                n2 = numbers[j]
                new_numbers = numbers[:i] + numbers[i+1:j] + numbers[j+1:]

                possible_numbers = [(n1 + n2, "{} + {}".format(n1, n2)),
                                    (n1 - n2, "{} - {}".format(n1, n2)),
                                    (n2 - n1, "{} - {}".format(n2, n1)),
                                    (n1 * n2, "{} * {}".format(n1, n2))]

                if n2 != 0:
                    possible_numbers.append((n1 / n2,
                                             "{} / {}".format(n1, n2)))
                if n1 != 0:
                    possible_numbers.append((n2 / n1,
                                             "{} / {}".format(n2, n1)))

                # Go through all six possible operations
                for number, expression in possible_numbers:

                    # Addition
                    new_target = target - number
                    expr = self.solve(new_numbers, new_target)
                    self.add_to_memory(new_numbers, new_target, expr)

                    if expr != IMPOSSIBLE:
                        return "({}) + {}".format(expression, expr)

                    # Subtraction
                    new_target = number - target
                    expr = self.solve(new_numbers, new_target)
                    self.add_to_memory(new_numbers, new_target, expr)

                    if expr != IMPOSSIBLE:
                        return "({}) - ({})".format(expression, expr)

                    # Subtraction 2 (n2 - n1)
                    new_target = number + target
                    expr = self.solve(new_numbers, new_target)
                    self.add_to_memory(new_numbers, new_target, expr)

                    if expr != IMPOSSIBLE:
                        return "({}) - ({})".format(expr, expression)

                    # Multiplication
                    if number != 0:
                        new_target = target / number
                        expr = self.solve(new_numbers, new_target)
                        self.add_to_memory(new_numbers, new_target, expr)
                        if expr != IMPOSSIBLE:
                            return "({}) * ({})".format(expression, expr)

                    if target != 0 and number != 0:
                        # Division
                        new_target = number / target
                        expr = self.solve(new_numbers, new_target)
                        self.add_to_memory(new_numbers, new_target, expr)
                        if expr != IMPOSSIBLE:
                            return "({}) / ({})".format(expression, expr)

                        # Division 2 (n2 / n1)
                        new_target = number * target
                        expr = self.solve(new_numbers, new_target)
                        self.add_to_memory(new_numbers, new_target, expr)
                        if expr != IMPOSSIBLE:
                            return "({}) / ({})".format(expr, expression)

                    new_numbers = new_numbers + (number,)
                    solved = self.solve(new_numbers, target)
                    if solved != IMPOSSIBLE:
                        solved = solved.replace(str(number),
                                                "(" + expression + ")", 1)
                        return solved
                    new_numbers = new_numbers[:-1]

        self.add_to_memory(numbers, target, IMPOSSIBLE)

        return IMPOSSIBLE


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    o = OperationGuess()
    print(o.solve((5, 2, 8), 9))

