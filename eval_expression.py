def eval_expression(s1: str) -> bool:
    """
    Evaluates the result of s1 and s2, and returns if they are equal.
    Precondition: s1 and s2 are string representations of a
    mathematical expression, and are both non-empty
    Post-condition: returns True if both mathematical expressions are
    equal to each other
    """
    return eval(s1.split('=')[0]) == eval(s1.split('=')[1])


if __name__ == "__main__":
    print(eval_expression("2 = (1 + 1 - 1)*2"))
    print(eval_expression("1 + 1 - 1 = 2"))
