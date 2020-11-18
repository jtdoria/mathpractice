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
