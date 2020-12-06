"""Functions which generate expressions. Design decisions based on Wolfram Alpha's Problem Generator"""
import random

"""------------------ ARITHMETIC ------------------"""


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


"""------------------ NUMBER THEORY ------------------"""


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


"""------------------ ALGEBRA ------------------"""


def algebra_radicals_add(diff):
    """ALGEBRA - RADICALS - ADD"""

    upper_bound = 10 ** (diff + 1)

    coefficient_1 = random.randint(1, upper_bound)
    index_1 = random.randint(2, 4)
    radicand_1 = random.randint(1, upper_bound)

    coefficient_2 = random.randint(1, upper_bound)
    index_2 = random.randint(2, 4)
    radicand_2 = random.randint(1, upper_bound)

    expr = f"{coefficient_1}\\sqrt[{index_1}]{{{radicand_1}}} + {coefficient_2}\\sqrt[{index_2}]{{{radicand_2}}}"

    return expr


def algebra_radicals_subtract(diff):
    """ALGEBRA - RADICALS - SUBTRACT"""

    upper_bound = 10 ** (diff + 1)

    coefficient_1 = random.randint(1, upper_bound)
    index_1 = random.randint(2, 4)
    radicand_1 = random.randint(1, upper_bound)

    coefficient_2 = random.randint(1, upper_bound)
    index_2 = random.randint(2, 4)
    radicand_2 = random.randint(1, upper_bound)

    expr = f"{coefficient_1}\\sqrt[{index_1}]{{{radicand_1}}} - {coefficient_2}\\sqrt[{index_2}]{{{radicand_2}}}"

    return expr


def algebra_radicals_multiply(diff):
    """ALGEBRA - RADICALS - MULTIPLY"""

    upper_bound = 10 ** (diff + 1)

    coefficient_1 = random.randint(1, upper_bound)
    index_1 = random.randint(2, 4)
    radicand_1 = random.randint(1, upper_bound)

    coefficient_2 = random.randint(1, upper_bound)
    index_2 = random.randint(2, 4)
    radicand_2 = random.randint(1, upper_bound)

    expr = f"{coefficient_1}\\sqrt[{index_1}]{{{radicand_1}}} * {coefficient_2}\\sqrt[{index_2}]{{{radicand_2}}}"

    return expr


def algebra_radicals_distribute(diff):
    """ALGEBRA - RADICALS - DISTRIBUTE"""

    upper_bound = 10 ** (diff + 1)

    coefficient_1 = random.randint(1, upper_bound)
    index_1 = random.randint(2, 4)
    radicand_1 = random.randint(1, upper_bound)

    coefficient_2 = random.randint(1, upper_bound)
    index_2 = random.randint(2, 4)
    radicand_2 = random.randint(1, upper_bound)

    coefficient_3 = random.randint(1, upper_bound)
    index_3 = random.randint(2, 4)
    radicand_3 = random.randint(1, upper_bound)

    expr = f"{coefficient_3}\\sqrt[{index_3}]{{{radicand_3}}} * " \
           f"( {coefficient_1}\\sqrt[{index_1}]{{{radicand_1}}} + {coefficient_2}\\sqrt[{index_2}]{{{radicand_2}}} )"

    return expr


def algebra_radicals_rationalize(diff):
    """ALGEBRA - RADICALS - RATIONALIZE"""
    upper_bound = 10 ** (diff + 1)
    sign = random.choice(["", "-"])
    numer = random.randint(0, upper_bound)

    coefficient = random.randint(1, upper_bound)
    index = random.randint(2, 4)
    radicand = random.randint(1, upper_bound)
    denom = f"{coefficient}\\sqrt[{index}]{{{radicand}}}"

    expr = f"{sign} \\frac{{{numer}}}{{{denom}}}"

    return expr


def algebra_radicals_simplify(diff):
    """ALGEBRA - RADICALS - SIMPLIFY"""

    if diff == 0:
        """Beginner: radical with max 3 digit radicand"""
        radicand = random.randint(1, 1000)
        expr = f"\\sqrt[]{{{radicand}}}"

    elif diff == 1:
        """Intermediate: same as beginner, but radicand is a quotient"""
        numer = random.randint(1, 1000)
        denom = random.randint(1, 1000)
        radicand = f"\\frac{{{numer}}}{{{denom}}}"
        expr = f"\\sqrt[]{{{radicand}}}"

    else:
        """Advanced: same as intermediate, but with max 4 digit numbers"""
        numer = random.randint(1, 10000)
        denom = random.randint(1, 10000)
        radicand = f"\\frac{{{numer}}}{{{denom}}}"
        expr = f"\\sqrt[]{{{radicand}}}"

    return expr


def algebra_complex_numbers_add(diff):
    """ALGEBRA - COMPLEX NUMBERS - ADD"""

    if diff == 0:
        """Beginner: (a + bi) + (c + di)"""
        coefficients = [random.randint(1, 10) for _ in range(4)]
        expr = f"({coefficients[0]} + {coefficients[1]}i) + ({coefficients[2]} + {coefficients[3]}i)"

    elif diff == 1:
        """Intermediate: same as beginner, but any two numbers will be quotients"""
        coefficients = [random.randint(1, 10) for _ in range(4)]
        targets = random.sample(range(4), 2)

        for target in targets:
            coefficients[target] = f"\\frac{{{coefficients[target]}}}{{{random.randint(1, 10)}}}"
        expr = f"({coefficients[0]} + {coefficients[1]}i) + ({coefficients[2]} + {coefficients[3]}i)"

    else:
        """Advanced: same as intermediate, but numbers will be max 3 digits long"""
        coefficients = [random.randint(1, 100) for _ in range(4)]
        targets = random.sample(range(4), 2)

        for target in targets:
            coefficients[target] = f"\\frac{{{coefficients[target]}}}{{{random.randint(1, 10)}}}"
        expr = f"({coefficients[0]} + {coefficients[1]}i) + ({coefficients[2]} + {coefficients[3]}i)"

    return expr


def algebra_complex_numbers_subtract(diff):
    """ALGEBRA - COMPLEX NUMBERS - SUBTRACT"""

    if diff == 0:
        """Beginner: (a + bi) - (c + di)"""
        coefficients = [random.randint(1, 10) for _ in range(4)]
        expr = f"({coefficients[0]} + {coefficients[1]}i) - ({coefficients[2]} + {coefficients[3]}i)"

    elif diff == 1:
        """Intermediate: same as beginner, but any two numbers will be quotients"""
        coefficients = [random.randint(1, 10) for _ in range(4)]
        targets = random.sample(range(4), 2)

        for target in targets:
            coefficients[target] = f"\\frac{{{coefficients[target]}}}{{{random.randint(1, 10)}}}"
        expr = f"({coefficients[0]} + {coefficients[1]}i) - ({coefficients[2]} + {coefficients[3]}i)"

    else:
        """Advanced: same as intermediate, but numbers will be max 3 digits long"""
        coefficients = [random.randint(1, 100) for _ in range(4)]
        targets = random.sample(range(4), 2)

        for target in targets:
            coefficients[target] = f"\\frac{{{coefficients[target]}}}{{{random.randint(1, 10)}}}"
        expr = f"({coefficients[0]} + {coefficients[1]}i) - ({coefficients[2]} + {coefficients[3]}i)"

    return expr


def algebra_complex_numbers_multiply(diff):
    """ALGEBRA - COMPLEX NUMBERS - MULTIPLY"""

    if diff == 0:
        """Beginner: (a + bi) * (c + di)"""
        coefficients = [random.randint(1, 10) for _ in range(4)]
        expr = f"({coefficients[0]} + {coefficients[1]}i) * ({coefficients[2]} + {coefficients[3]}i)"

    elif diff == 1:
        """Intermediate: same as beginner, but any two numbers will be quotients"""
        coefficients = [random.randint(1, 10) for _ in range(4)]
        targets = random.sample(range(4), 2)

        for target in targets:
            coefficients[target] = f"\\frac{{{coefficients[target]}}}{{{random.randint(1, 10)}}}"
        expr = f"({coefficients[0]} + {coefficients[1]}i) * ({coefficients[2]} + {coefficients[3]}i)"

    else:
        """Advanced: same as intermediate, but numbers will be max 3 digits long"""
        coefficients = [random.randint(1, 100) for _ in range(4)]
        targets = random.sample(range(4), 2)

        for target in targets:
            coefficients[target] = f"\\frac{{{coefficients[target]}}}{{{random.randint(1, 10)}}}"
        expr = f"({coefficients[0]} + {coefficients[1]}i) * ({coefficients[2]} + {coefficients[3]}i)"

    return expr


def algebra_complex_numbers_divide(diff):
    """ALGEBRA - COMPLEX NUMBERS - DIVIDE"""

    if diff == 0:
        """Beginner: (a + bi) / (c + di)"""
        coefficients = [random.randint(1, 10) for _ in range(4)]
        expr = f"({coefficients[0]} + {coefficients[1]}i) / ({coefficients[2]} + {coefficients[3]}i)"

    elif diff == 1:
        """Intermediate: same as beginner, but any two numbers will be quotients"""
        coefficients = [random.randint(1, 10) for _ in range(4)]
        targets = random.sample(range(4), 2)

        for target in targets:
            coefficients[target] = f"\\frac{{{coefficients[target]}}}{{{random.randint(1, 10)}}}"
        expr = f"({coefficients[0]} + {coefficients[1]}i) / ({coefficients[2]} + {coefficients[3]}i)"

    else:
        """Advanced: same as intermediate, but numbers will be max 3 digits long"""
        coefficients = [random.randint(1, 100) for _ in range(4)]
        targets = random.sample(range(4), 2)

        for target in targets:
            coefficients[target] = f"\\frac{{{coefficients[target]}}}{{{random.randint(1, 10)}}}"
        expr = f"({coefficients[0]} + {coefficients[1]}i) / ({coefficients[2]} + {coefficients[3]}i)"

    return expr


def algebra_complex_numbers_find_the_norm(diff):
    """ALGEBRA - COMPLEX NUMBERS - FIND THE NORM"""

    if diff == 0:
        """Beginner: Find the norm of a + bi"""
        coefficients = [random.randint(1, 10) for _ in range(2)]
        expr = f"Find the norm of {coefficients[0]} + {coefficients[1]}i"

    elif diff == 1:
        """Intermediate: same as beginner, but a is a quotient"""
        coefficients = [f"\\frac{{{random.randint(1, 10)}}}{{{random.randint(1, 10)}}}", random.randint(1, 10)]
        expr = f"Find the norm of {coefficients[0]} + {coefficients[1]}i"

    else:
        """Advanced: same as beginner, but b is a radical"""
        coefficients = [random.randint(1, 10) for _ in range(2)]
        expr = f"Find the norm of {coefficients[0]} + \\sqrt[]{{{coefficients[1]}}} * i"

    return expr


def algebra_polynomials_evaluate_at_a_point(diff):
    """ALGEBRA - POLYNOMIALS - EVALUATE AT A POINT"""

    if diff == 0:
        """Beginner: x^2"""
        coefficients = [random.randint(1, 10) for _ in range(2)]
        constant = random.randint(1, 10)
        point = random.randint(0, 10)
        expr = f"Evaluate\\ {coefficients[0]}x^{2} + {coefficients[1]}x + {constant}\\ at\\ x = {point}"

    elif diff == 1:
        """Intermediate: x^3"""
        coefficients = [random.randint(1, 10) for _ in range(3)]
        constant = random.randint(1, 10)
        point = random.randint(0, 10)
        expr = f"Evaluate\\ {coefficients[0]}x^{3} + {coefficients[1]}x^{2} + {coefficients[2]}x + {constant}\\ at\\ " \
               f"x = {point} "

    else:
        """Advanced: x^4"""
        coefficients = [random.randint(1, 10) for _ in range(4)]
        constant = random.randint(1, 10)
        point = random.randint(0, 10)
        expr = f"Evaluate\\ {coefficients[0]}x^{4} + {coefficients[1]}x^{3} + {coefficients[2]}x^{2} + " \
               f"{coefficients[3]}x + {constant}\\ at\\ x = {point} "

    return expr


def algebra_polynomials_add(diff):
    """ALGEBRA - POLYNOMIALS - ADD"""

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_polynomials_subtract(diff):
    """ALGEBRA - POLYNOMIALS - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_polynomials_expand(diff):
    """ALGEBRA - POLYNOMIALS - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_polynomials_factor(diff):
    """ALGEBRA - POLYNOMIALS - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_polynomials_multiply_monomial_and_polynomial(diff):
    """ALGEBRA - POLYNOMIALS - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_polynomials_multiply_two_polynomials(diff):
    """ALGEBRA - POLYNOMIALS - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_polynomials_binomial_expansion(diff):
    """ALGEBRA - POLYNOMIALS - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_polynomials_horizontal_axis_intercepts(diff):
    """ALGEBRA - POLYNOMIALS - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_quadratic_polynomials_expand(diff):
    """ALGEBRA - QUADRATIC POLYNOMIALS - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_quadratic_polynomials_factor(diff):
    """ALGEBRA - QUADRATIC POLYNOMIALS - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_quadratic_polynomials_complete_the_square(diff):
    """ALGEBRA - QUADRATIC POLYNOMIALS - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_integers_one_step_equations(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_integers_two_step_equations(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_rationals_one_step_equations(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_rationals_two_step_equations(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_multi_step_equations(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_absolute_values_integer_equations(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_absolute_values_rational_equations(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_absolute_values_radical_equations(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_quadratic_equations_completed_squares(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_quadratic_equations_integer_solutions(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_quadratic_equations_difference_of_squares(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_quadratic_equations_complex_number_solutions(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_quadratic_equations_radical_solutions(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_general_factored_equations(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_general_polynomial_equations(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_general_multi_variate_equations(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_exponents_and_logarithms_exponential_equations(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_exponents_and_logarithms_logarithmic_equations(diff):
    """ALGEBRA - EQUATION SOLVING - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_systems_of_equations_systems_of_two_equations(diff):
    """ALGEBRA - SYSTEMS OF EQUATIONS - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_systems_of_equations_systems_of_three_equations(diff):
    """ALGEBRA - SYSTEMS OF EQUATIONS - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


def algebra_equation_solving_systems_of_equations_systems_of_four_equations(diff):
    """ALGEBRA - SYSTEMS OF EQUATIONS - """

    if diff == 0:
        expr = f""

    elif diff == 1:
        expr = f""

    else:
        expr = f""

    return expr


"""------------------ CALCULUS ------------------"""
"""------------------ LINEAR ALGEBRA ------------------"""
"""------------------ STATISTICS ------------------"""
