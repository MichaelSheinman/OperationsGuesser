IMPOSSIBLE = "Impossible"


def solve2digits(numbers: list, target: int) -> str:
    """Verify whether a list of 2 numbers can be made
    equal to target.
    Precondition: numbers is a list of two integers
    Postcondition: Returns either a mathematical expression containing
    both integers that equals target, or IMPOSSIBLE if no such
    expression exists.
    >>> solve2digits([0, 1], 0)
    '0 * 1'
    >>> solve2digits([8, 2], 4)
    '8 / 2'
    >>> solve2digits([8, 2], 99)
    'Impossible'
    """
    number1 = numbers[0]
    number2 = numbers[1]

    if number1 + number2 == target:
        return "{} + {}".format(number1, number2)
    if number1 - number2 == target:
        return "{} - {}".format(number1, number2)
    if number2 - number1 == target:
        return "{} - {}".format(number2, number1)
    if number1 * number2 == target:
        return "{} * {}".format(number1, number2)
    if number2 != 0:
        if number1 / number2 == target:
            return "{} / {}".format(number1, number2)
    if number1 != 0:
        if number2 / number1 == target:
            return "{} / {}".format(number2, number1)
    return IMPOSSIBLE


# TODO solving algorithm may have to be updated after optimization
def solve(numbers: list, target: int) -> str:
    """
    Solving Algorithm:
    Take two digits at a time, compute their result.
    Then see if the rest of the numbers can get to
    those two digits.
    Precondition: numbers is a list of integers
    Postcondition: Returns either a mathematical expression containing
    all the integers in number equalling target, or IMPOSSIBLE, if no
    such expression exists.
    >>> solve([1, 7, 5, 2], 9)
    '((1 + 7) / 2) + 5'
    >>> solve([1, 7, 5, 2], 999)
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
        return solve2digits(numbers, target)

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            n1 = numbers[i]
            n2 = numbers[j]
            new_numbers = numbers.copy()
            new_numbers.remove(n1)
            new_numbers.remove(n2)

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
                expr = solve(new_numbers, new_target)

                if expr != IMPOSSIBLE:
                    return "({}) + {}".format(expression, expr)

                # Subtraction
                new_target = number - target
                expr = solve(new_numbers, new_target)
                if expr != IMPOSSIBLE:
                    if expr.isdecimal():
                        return "({}) - {}".format(expression, expr)
                    return "({}) - ({})".format(expression, expr)

                # Subtraction 2 (n2 - n1)
                new_target = number + target
                expr = solve(new_numbers, new_target)
                if expr != IMPOSSIBLE:
                    if expr.isdecimal():
                        return "{} - ({})".format(expr, expression)
                    return "({}) - ({})".format(expr, expression)


                # Multiplication
                if number != 0:
                    new_target = target / number
                    expr = solve(new_numbers, new_target)
                    if expr != IMPOSSIBLE:
                        if expr.isdecimal():
                            return "({}) * {}".format(expression, expr)
                        return "({}) * ({})".format(expression, expr)

                if target != 0 and number != 0:
                    # Division
                    new_target = number / target
                    expr = solve(new_numbers, new_target)
                    if expr != IMPOSSIBLE:
                        if expr.isdecimal():
                            return "({}) / {}".format(expression, expr)
                        return "({}) / ({})".format(expression, expr)

                    # Division 2 (n2 / n1)
                    new_target = number * target
                    expr = solve(new_numbers, new_target)
                    if expr != IMPOSSIBLE:
                        if expr.isdecimal():
                            return "{} / ({})".format(expr, expression)
                        return "({}) / ({})".format(expr, expression)

                new_numbers.append(number)
                solved = solve(new_numbers, target)
                if solved != IMPOSSIBLE:
                    if expression.isdecimal():
                        solved = solved.replace(str(number), expression, 1)
                    else:
                        solved = solved.replace(str(number),
                                            "(" + expression + ")", 1)
                    return solved
                new_numbers.remove(number)
    return IMPOSSIBLE


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(solve([1, 7, 5, 2], 9))
    print(solve([1, 7, 5, 2], 999))
ro