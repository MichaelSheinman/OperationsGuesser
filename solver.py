def solve(numbers: list, target: int) -> str:
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

        # Division
        if target != 0:
            new_target = item / target
            expr = solve(numbers[:ii] +
                         numbers[ii + 1:], new_target)
            if expr != "Impossible":
                return "{} / ({})".format(item, expr)

    return "Impossible"


print(solve([4, 3, 8], 4))
