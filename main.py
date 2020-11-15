"""Functions responsible for building and traversing the tree."""

import definitions as defn
import logging.config
import logging_config.config as lc
import re
import tree


# Logging
logging.config.dictConfig(lc.config_dict)
logger = logging.getLogger('my_logger')


def build_tree(expr):
    logger.info(f"Called build_tree.")

    # Initialize the tree and stack.
    root = tree.Node()
    p_stack = tree.Stack()
    p_stack.push(root)

    # Step 1 and 2: expression string and list
    logger.debug(f"expr = {expr}")
    expr_list = expr.split()
    logger.debug(f"expr_lst = {expr_list}")

    # Step 3: Map expression element to mathematical object.
    regex_to_class_dict = {
        r"^[0-9]+$": defn.Integer,
        r"^[0-9]+\.[0-9]+$": defn.Decimal,
        r"^\+$": defn.Add,
        r"^\-$": defn.Subtract,
        r"^\*$": defn.Multiply,
        r"^\/$": defn.Divide,
        r"^{": defn.Power,
        r"\\frac": defn.Fraction,
        r"\\sqrt": defn.SquareRoot,
        r"\\log": defn.Logarithm
    }

    logger.debug("Begin parsing expression list...")
    for element in expr_list:
        for pattern in regex_to_class_dict:
            if re.search(pattern, element):
                logger.debug(f"       '{element}'  : {regex_to_class_dict[pattern]}.")

                # Steps 4, 5, and 6
                component = regex_to_class_dict[pattern](element)
                # logger.debug(f"Verify obj created: {component}, type {type(component)}.")
                component.grow(p_stack)

    root_node = p_stack.pop(0)

    return root_node


def traverse(node):
    result = ""
    if node.get_children():
        num_of_children = len(node.get_children())
        for i in range(num_of_children):
            result += str(traverse(node.get_child(i)))
            if (i != num_of_children - 1) and isinstance(node.get_child(i + 1).get_cargo(), defn.Subtract):
                result += "-"
            if (i != num_of_children - 1) and not isinstance(node.get_child(i + 1).get_cargo(), defn.Subtract):
                result += str(node.get_cargo())
    else:
        return node.get_cargo()
    return result


def insert_spaces(expr):
    temp = list(expr)
    for i in range(len(expr)):
        temp.insert(2 * i + 1, " ")
    temp.pop()
    expr = "".join(temp)
    return expr

