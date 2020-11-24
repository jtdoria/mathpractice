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
    """ARITHMETIC - ORDER OF OPERATIONS - BASIC OPERATIONS"""
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


def gen_arithmetic_order_of_operations_include_exponents(diff):
    """ARITHMETIC - ORDER OF OPERATIONS - INCLUDE EXPONENTS"""
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

    # INSERT EXPONENT
    r_index = random.randint(0, (len(operands) - 1))
    target = operands[r_index] + "^{2}"
    operands[r_index] = target

    expression_list = operands[:]
    for i in range(num_of_operations):
        expression_list.insert(2 * i + 1, operations[i])

    expression_string = ' '.join(expression_list)
    print(expression_list)
    return expression_string


def gen_arithmetic_order_of_operations_include_parentheses(diff):
    """ARITHMETIC - ORDER OF OPERATIONS - INCLUDE PARENTHESES"""
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

    # INSERT PARENTHESES
    print(expression_list)

    open_pos = 2 * random.randint(0, int((len(expression_list) - 1) / 2))
    print(f"open_pos:  {open_pos}")
    expression_list.insert(open_pos, '(')

    close_pos = open_pos + 2 * random.randint(1, int((len(expression_list) - open_pos) / 2))
    print(f"close_pos: {close_pos}")
    expression_list.insert(close_pos, ')')

    expression_string = ' '.join(expression_list)
    return expression_string


"""ARITHMETIC - FRACTIONS"""


def gen_arithmetic_fractions_add_with_common_denominators(diff):
    """ARITHMETIC - FRACTIONS - ADD WITH COMMON DENOMINATORS"""
    operation = "+"
    upper_bound = 10 ** (diff + 1)
    numer_1 = random.randint(0, upper_bound)
    numer_2 = random.randint(0, upper_bound)
    denom = random.randint(0, upper_bound)
    expr = f"\\frac{{{numer_1}}}{{{denom}}} {operation} \\frac{{{numer_2}}}{{{denom}}}"
    return expr


def gen_arithmetic_fractions_subtract_with_common_denominators(diff):
    """ARITHMETIC - FRACTIONS - SUBTRACT WITH COMMON DENOMINATORS"""
    operation = "-"
    upper_bound = 10 ** (diff + 1)
    numer_1 = random.randint(0, upper_bound)
    numer_2 = random.randint(0, upper_bound)
    denom = random.randint(0, upper_bound)
    expr = f"\\frac{{{numer_1}}}{{{denom}}} {operation} \\frac{{{numer_2}}}{{{denom}}}"
    return expr


def gen_arithmetic_fractions_add_with_uncommon_denominators(diff):
    """ARITHMETIC - FRACTIONS - ADD WITH UNCOMMON DENOMINATORS"""
    operation = "+"
    upper_bound = 10 ** (diff + 1)
    numer_1 = random.randint(0, upper_bound)
    numer_2 = random.randint(0, upper_bound)
    denom_1 = random.randint(0, upper_bound)
    denom_2 = random.randint(0, upper_bound)
    expr = f"\\frac{{{numer_1}}}{{{denom_1}}} {operation} \\frac{{{numer_2}}}{{{denom_2}}}"
    return expr


def gen_arithmetic_fractions_subtract_with_uncommon_denominators(diff):
    """ARITHMETIC - FRACTIONS - SUBTRACT WITH UNCOMMON DENOMINATORS"""
    operation = "-"
    upper_bound = 10 ** (diff + 1)
    numer_1 = random.randint(0, upper_bound)
    numer_2 = random.randint(0, upper_bound)
    denom_1 = random.randint(0, upper_bound)
    denom_2 = random.randint(0, upper_bound)
    expr = f"\\frac{{{numer_1}}}{{{denom_1}}} {operation} \\frac{{{numer_2}}}{{{denom_2}}}"
    return expr


def gen_arithmetic_fractions_multiply(diff):
    """ARITHMETIC - FRACTIONS - MULTIPLY"""
    operation = "*"
    upper_bound = 10 ** (diff + 1)
    numer_1 = random.randint(0, upper_bound)
    numer_2 = random.randint(0, upper_bound)
    denom_1 = random.randint(0, upper_bound)
    denom_2 = random.randint(0, upper_bound)
    expr = f"\\frac{{{numer_1}}}{{{denom_1}}} {operation} \\frac{{{numer_2}}}{{{denom_2}}}"
    return expr


def gen_arithmetic_fractions_divide(diff):
    """ARITHMETIC - FRACTIONS - DIVIDE"""
    operation = "/"
    upper_bound = 10 ** (diff + 1)
    numer_1 = random.randint(0, upper_bound)
    numer_2 = random.randint(0, upper_bound)
    denom_1 = random.randint(0, upper_bound)
    denom_2 = random.randint(0, upper_bound)
    expr = f"\\frac{{{numer_1}}}{{{denom_1}}} {operation} \\frac{{{numer_2}}}{{{denom_2}}}"
    return expr


def gen_arithmetic_fractions_simplify(diff):
    """ARITHMETIC - FRACTIONS - SIMPLIFY"""

    upper_bound = 10 ** (diff + 1)
    common_divisor = random.randint(1, 10)
    numer = random.randint(1, upper_bound)
    denom = random.randint(1, upper_bound)

    numer = numer * common_divisor
    denom = denom * common_divisor

    expr = f"\\frac{{{numer}}}{{{denom}}}"
    return expr


"""NUMBER THEORY"""


def number_theory_integers_divisibility_test(diff):
    """NUMBER THEORY - INTEGERS - DIVISIBILITY TEST"""
    """Ways to ask the question:
    1 - Is a divisible by b?"""
    upper_bound = 10 ** (diff + 2)
    dividend = random.randint(20, upper_bound)
    divisor = random.randint(1, 10)
    word_expr = f"Is {dividend} divisible by {divisor}?"
    return word_expr


def number_theory_integers_primality_test(diff):
    """NUMBER THEORY - INTEGERS - PRIMALITY TEST"""
    """Ways to ask the question:
    1 - Is x a prime number?
    2 - Are 1 and x the only positive numbers that x can be divided by?
    3 - 1 and x are the only positive numbers that divide x. True or False?
    4 - x is one of the prime numbers. True or False?"""
    upper_bound = 10 ** (diff + 1)
    candidate = random.randint(1, upper_bound)
    word_expr = f"Is {candidate} a prime number?"
    return word_expr


def number_theory_integers_prime_factorization(diff):
    """NUMBER THEORY - INTEGERS - PRIME FACTORIZATION"""
    """Ways to ask the question:
    1 - Factor x into its prime factors."""
    upper_bound = 10 ** (diff + 1)
    candidate = random.randint(4, upper_bound)
    word_expr = f"Factor {candidate} into its prime factors."
    return word_expr


def number_theory_integers_divisors(diff):
    """NUMBER THEORY - INTEGERS - DIVISORS"""
    """Ways to ask the question:
    1 - List all divisors of x.
    eg x = 16, => [1, 2, 3, 4, 8, 16]"""
    upper_bound = 10 ** (diff + 1)
    candidate = random.randint(1, upper_bound)
    word_expr = f"List all divisors of {candidate}."
    return word_expr


def number_theory_integers_greatest_common_divisor(diff):
    """NUMBER THEORY - INTEGERS - GREATEST COMMON DIVISOR"""
    """Ways to ask the question:
    1 - Find the greatest common divisor of a and b."""
    upper_bound = 10 ** (diff + 1)
    a = random.randint(1, upper_bound)
    b = random.randint(1, upper_bound)
    word_expr = f"Find the greatest common divisor of {a} and {b}."
    return word_expr


def number_theory_integers_least_common_multiple(diff):
    """NUMBER THEORY - INTEGERS - LEAST COMMON MULTIPLE"""
    """Ways to ask the question:
        1 - Find the least common multiple of a and b."""
    upper_bound = 10 ** (diff + 1)
    a = random.randint(1, upper_bound)
    b = random.randint(1, upper_bound)
    word_expr = f"Find the least common multiple of {a} and {b}."
    return word_expr


def number_theory_integers_relatively_prime_test(diff):
    """NUMBER THEORY - INTEGERS - RELATIVELY PRIME TEST"""
    """Ways to ask the question:
    1 - Is 1 the only positive number that divides both a and b?
    2 - Are a and b relatively prime?
    3 - Is a coprime with b?
    4 - Are a and b mutually prime?
    The solution is to find all prime factors of a and b and 
    return True if they don't share any (except the number 1)"""
    upper_bound = 10 ** (diff + 2)
    a = random.randint(1, upper_bound)
    b = random.randint(1, upper_bound)
    word_expr = f"Is 1 the only positive number that divides both {a} and {b}?"
    return word_expr
