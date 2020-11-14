import logging.config
import logging_config.config as lc
import random
import main


# Logging
logging.config.dictConfig(lc.config_dict)
logger = logging.getLogger('my_logger')


# Banks
latex_bank = {
    'operators': (
        '+',
        '-',
        '*',
        '/',
    ),
}


def generate_expression(n_operations):
    """
    :param n_operations: int representing the number of operations in the expression
    :return: expression_string: str of latex ready for the build_tree function
    """
    operators = [o for o in random.choices(latex_bank['operators'], k=n_operations)]
    operands = [str(random.randint(0, 9)) for _ in range(n_operations + 1)]
    expression_list = operands[:]

    for i in range(len(operators)):
        expression_list.insert(2 * i + 1, operators[i])

    expression_string = ' '.join(expression_list)
    logger.debug(f"Generated expression: '{expression_string}'")
    return expression_string


def generate_test(*, n_cases, n_operations):
    # TODO: better way to handle n_operations parameter here
    test = [generate_expression(n_operations) for _ in range(n_cases)]
    logger.debug(f"Generated test with {len(test)} expressions.")
    return test


def test_node_traversal(original_expression):
    tree = main.build_tree(original_expression)
    traversal = main.traverse(tree)
    result = main.insert_spaces(traversal)  # TODO: better way to handle insert_spaces
    try:
        assert original_expression == result, f"original: '{original_expression}', result: '{result}'"
    except Exception as e:
        logger.exception(e)
    return None


def run_test(test):
    logger.info(f"Running test with {len(test)} cases.")
    test_no = 1
    for case in test:
        logger.info(f"Case No. {test_no}")
        test_node_traversal(case)
        test_no += 1
    return None
