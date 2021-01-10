def solve(numbers: list, target: int) -> str:
    """Solving Algorithm:
    Take the first digit, then compute the
    required value recursively.
    """
    if len(numbers) == 1:
        if numbers[0] == target:
            return str(numbers[0])
        else:
            return "Impossible"

    for ii, item in enumerate(numbers):
        # Addition
        new_target = target - item

        expr = solve(numbers[:ii] + numbers[ii + 1:], new_target)
        if expr != "Impossible":
            return "{} + ({})".format(item, expr)

        # Multiplication
        if item != 0:
            new_target = target / item
            if new_target == int(new_target):
                expr = solve(numbers[:ii] +
                             numbers[ii + 1:], new_target)
                if expr != "Impossible":
                    return "{} * ({})".format(item, expr)

        # Subtraction
        # item - newTarget = target
        new_target = item - target
        expr = solve(numbers[:ii] +
                     numbers[ii + 1:], new_target)
        if expr != "Impossible":
            return "{} - ({})".format(item, expr)

        # Subtraction
        # item - newTarget = target
        new_target = target + item
        expr = solve(numbers[:ii] +
                     numbers[ii + 1:], new_target)
        if expr != "Impossible":
            return "({}) - {}".format(expr, item)

        # Division
        if target != 0:
            new_target = item / target
            expr = solve(numbers[:ii] +
                         numbers[ii + 1:], new_target)
            if expr != "Impossible":
                return "{} / ({})".format(item, expr)

    return "Impossible"


def solve2Digits(numbers: list, target: int) -> str:
    """Verify whether a list of 2 numbers can be made
    equal to target"""
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
    return "Impossible"


def solve2(numbers: list, target: int) -> str:
    """Solving Algorithm:
    Take two digits at a time, compute their result.
    Then see if the rest of the numbers can get to
    those two digits.
    """
    if len(numbers) == 0:
        return ''
    if len(numbers) == 1:
        if numbers[0] == target:
            return "{}".format(numbers[0])
        else:
            return "Impossible"
    if len(numbers) == 2:
        return solve2Digits(numbers, target)

    directSolution = solve(numbers, target)
    if directSolution != "Impossible":
        return directSolution

    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            n1 = numbers[i]
            n2 = numbers[j]
            new_numbers = numbers.copy()
            new_numbers.remove(n1)
            new_numbers.remove(n2)

            # Addition
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

            for number, expression in possible_numbers:
                # Do the four operations

                # Addition
                new_target = target - number
                expr = solve2(new_numbers, new_target)

                if expr != "Impossible" and expr != '':
                    return "({}) + {}".format(expression, expr)


                # Subtraction
                new_target = number - target
                expr = solve2(new_numbers, new_target)
                if expr != "Impossible" and expr != '':
                    return "({}) - ({})".format(expression, expr)

                # Subtraction 2
                new_target = number + target
                expr = solve2(new_numbers, new_target)
                if expr != "Impossible" and expr != '':
                    return "({}) - ({})".format(expr, expression)

                # Multiplication
                if number != 0:
                    new_target = target / number
                    expr = solve2(new_numbers, new_target)
                    if expr != "Impossible" and expr != '':
                        return "({}) * ({})".format(expression, expr)

                # Division
                if target != 0:
                    new_target = number / target
                    expr = solve2(new_numbers, new_target)
                    if expr != "Impossible" and expr != '':
                        return "({}) / ({})".format(expression, expr)

                # Division 2
                if number != 0:
                    new_target = number * target
                    expr = solve2(new_numbers, new_target)
                    if expr != "Impossible" and expr != '':
                        return "({}) / ({})".format(expr, expression)

                new_numbers.append(number)
                solved = solve2(new_numbers, target)
                if solved != "Impossible":
                    solved = solved.replace(str(number),"(" + expression + ")", 1)
                    return solved
                new_numbers.remove(number)
    return "Impossible"


if __name__ == '__main__':
    val = solve2([55, 2, 3, 1, 18], 360)
    print(val)
