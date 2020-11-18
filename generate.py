"""Functions which generate expressions. Design decisions based on Wolfram Alpha's Problem Generator"""
import random


def gen_arithmetic(operation, diff):
    """Function to generate expressions with the arithmetic operations of addition, subtraction, multiplication, and
    division.

    Parameters
        operation string: "+", "-", "*', or "/"
    Return
        expr string: expression string with latex formatting
    """
    upper_bound = 10 ** (diff + 1)
    op1 = random.randint(0, upper_bound)
    op2 = random.randint(0, upper_bound)
    expr = f"{op1} {operation} {op2}"
    return expr


def gen_order_of_operations(diff):
    """Function to generate expressions of various length with the arithmetic operations of addition, subtraction,
    multiplication, and division.

    Parameters
        diff int: difficulty level 0, 1, or 2.
    Return
        expr string: expression string with latex formatting
    """
    latex_bank = {
        'operations': (
            '+',
            '-',
            '*',
            '/',
        ),
    }

    num_of_operations = 3 + diff
    num_of_operands = num_of_operations + 1

    operations = [operation for operation in random.choices(latex_bank['operations'], k=num_of_operations)]
    operands = [str(random.randint(0, 10)) for _ in range(num_of_operands)]

    expression_list = operands[:]
    for i in range(num_of_operations):
        expression_list.insert(2 * i + 1, operations[i])

    expression_string = ' '.join(expression_list)
    return expression_string
