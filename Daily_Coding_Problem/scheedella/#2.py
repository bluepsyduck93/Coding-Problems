'''
Given an arithmetic expression in Reverse Polish Notation, write a program to evaluate it.

The expression is given as a list of numbers and operands. For example: [5, 3, '+'] should return 5 + 3 = 8.

For example, [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-'] should return 5, since it is equivalent to ((15 / (7 - (1 + 1))) * 3) - (2 + (1 + 1)) = 5.

You can assume the given expression is always valid.
'''


def evaluate(lst):
    stack = []
    for elem in lst:
        if not str(elem).isdigit():
            x = stack.pop()
            y = stack.pop()
            stack.append(eval(f'{x} {elem} {y}'))
        else:
            stack.append(elem)

    return stack.pop()
