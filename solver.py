from typing import Optional

IMPOSSIBLE = "Impossible"


def _upper_bound(numbers: tuple) -> int:
    """
    A private helper to generate an upper bound
    for the operations made with numbers
    >>> _upper_bound((1, 3, 6)) >= 24
    True
    """
    prod = 1
    for number in numbers:
        prod *= abs(number) + 1
    return prod


def _sort_tuple(numbers: tuple) -> tuple:
    """
    A private helper to sort a tuple and return a new
    sorted tuple.
    """
    return tuple(sorted(list(numbers)))


class OperationGuess:

    def __init__(self):
        self.sequence_to_target = {}
        # sequence: {target: result}

    def reset_memory(self):
        self.sequence_to_target.clear()

    def solve2digits(self, numbers: tuple, target: int) -> str:
        """Verify whether a list of 2 numbers can be made
        equal to target.
        Precondition: numbers is a list of two integers
        Postcondition: Returns either a mathematical expression containing
        both integers that equals target, or IMPOSSIBLE if no such
        expression exists.
        >>> og = OperationGuess()
        >>> og.solve2digits((0, 1), 0)
        '0 * 1'
        >>> og.solve2digits((8, 2), 4)
        '8 / 2'
        >>> og.solve2digits((8, 2), 99)
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
        {tuple: {target: string representation of solution} }
        """
        sequence = _sort_tuple(sequence)

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
        >>> og = OperationGuess()
        >>> og.solve((1, 2), 3)
        '1 + 2'
        >>> og.solve((1, 7, 5, 2), 999)
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

        memory_status = self.check_memory(numbers, target)
        if memory_status:
            return memory_status

        ub = _upper_bound(numbers)
        lb = -ub
        if target > ub:
            self.add_to_memory(numbers, target, IMPOSSIBLE)
            return IMPOSSIBLE
        if target < lb:
            self.add_to_memory(numbers, target, IMPOSSIBLE)
            return IMPOSSIBLE

        for i in range(len(numbers)):

            for j in range(i+1, len(numbers)):
                memory_status = self.check_memory(numbers, target)
                if memory_status:
                    return memory_status

                n1 = numbers[i]
                n2 = numbers[j]
                new_numbers = numbers[:i] + numbers[i+1:j] + numbers[j+1:]

                possible_numbers = [(n1 + n2, "{} + {}".format(n1, n2), '+'),
                                    (n1 - n2, "{} - {}".format(n1, n2), '-'),
                                    (n2 - n1, "{} - {}".format(n2, n1), '-'),
                                    (n1 * n2, "{} * {}".format(n1, n2), '*')]

                if n2 != 0:
                    possible_numbers.append((n1 / n2,
                                             "{} / {}".format(n1, n2), '/'))
                if n1 != 0:
                    possible_numbers.append((n2 / n1,
                                             "{} / {}".format(n2, n1), '/'))

                # Go through all six possible operations
                for number, expression, sign in possible_numbers:

                    # Addition
                    new_target = target - number
                    expr = self.solve(new_numbers, new_target)
                    self.add_to_memory(new_numbers, new_target, expr)

                    if expr != IMPOSSIBLE:
                        return "{} + {}".format(expression, expr)

                    # Subtraction
                    new_target = number - target
                    expr = self.solve(new_numbers, new_target)
                    self.add_to_memory(new_numbers, new_target, expr)

                    if expr != IMPOSSIBLE:
                        if expr.isdecimal():
                            return "{} - {}".format(expression, expr)
                        return "{} - ({})".format(expression, expr)

                    # Subtraction 2 (n2 - n1)
                    new_target = number + target
                    expr = self.solve(new_numbers, new_target)
                    self.add_to_memory(new_numbers, new_target, expr)

                    if expr != IMPOSSIBLE:
                        if sign == '*' or sign == '/':
                            return "{} - {}".format(expr, expression)
                        return "{} - ({})".format(expr, expression)

                    # Multiplication
                    if number != 0:
                        new_target = target / number
                        expr = self.solve(new_numbers, new_target)
                        self.add_to_memory(new_numbers, new_target, expr)
                        if expr != IMPOSSIBLE:
                            if expr.isdecimal() and (sign == '+' or sign == '-'):
                                return "({}) * {}".format(expression, expr)
                            elif expr.isdecimal() and (sign == '*' or sign == '/'):
                                return "{} * {}".format(expression, expr)
                            elif not expr.isdecimal() and (sign == '*' or sign == '/'):
                                return "{} * ({})".format(expression, expr)
                            return "({}) * ({})".format(expression, expr)

                    if target != 0 and number != 0:
                        # Division
                        new_target = number / target
                        expr = self.solve(new_numbers, new_target)
                        self.add_to_memory(new_numbers, new_target, expr)
                        if expr != IMPOSSIBLE:
                            if expr.isdecimal() and (sign == '+' or sign == '-'):
                                return "({}) / {}".format(expression, expr)
                            elif expr.isdecimal() and (sign == '*' or sign == '/'):
                                return "{} / {}".format(expression, expr)
                            elif not expr.isdecimal() and (sign == '*' or sign == '/'):
                                return "{} / ({})".format(expression, expr)
                            return "({}) / ({})".format(expression, expr)

                        # Division 2 (n2 / n1)
                        new_target = number * target
                        expr = self.solve(new_numbers, new_target)
                        self.add_to_memory(new_numbers, new_target, expr)
                        if expr != IMPOSSIBLE:
                            if expr.isdecimal():
                                return "{} / ({})".format(expr, expression)
                            return "({}) / ({})".format(expr, expression)

                    # If everything else failed, add the current number
                    # Recursively find an expression with the other number
                    new_numbers = new_numbers + (number,)
                    solved = self.solve(new_numbers, target)
                    if solved != IMPOSSIBLE:
                        to_replace = solved.find(str(number))
                        if (solved[to_replace + 1: to_replace + 3] == ' +' or \
                                solved[to_replace + 1: to_replace + 3] == ' -' or to_replace == len(solved) - 1 or \
                                solved[to_replace + 1] == ')') and \
                                (solved[to_replace - 2: to_replace] == '+ ' or \
                                 (solved[to_replace - 2: to_replace] == '- ' and (sign != '-' or sign != '+')) or \
                                 to_replace == 0 or solved[to_replace - 1] == '('):
                            solved = solved.replace(str(number), expression, 1)
                        elif (sign == '*' or sign == '/') and solved[to_replace - 2: to_replace] != '/ ':
                            solved = solved.replace(str(number), expression, 1)
                        else:
                            solved = solved.replace(str(number), "(" + expression + ")", 1)
                        return solved
                    new_numbers = new_numbers[:-1]

        self.add_to_memory(numbers, target, IMPOSSIBLE)

        return IMPOSSIBLE


if __name__ == '__main__':
    import doctest
    doctest.testmod()

