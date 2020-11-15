"""Functions responsible for going about th business of solving one of these damned expressions."""

import logging.config
import logging_config.config as lc
import main
import definitions as defn
import exceptions
import re


# Logging
logging.config.dictConfig(lc.config_dict)
logger = logging.getLogger('my_logger')


def collect_leaf_nodes(node, lf_nds=None, level=0):
    """
    Arguments:
        node: (tree.Node object) to provide starting node from which to begin evaluation.
        lf_nds: (list) to contain the leaf nodes.
        level: (int) to keep track of tree depth level.
    Returns:
        leaf_nodes: (list of tuples) list containing tuples of all leaf nodes and their respective depth level in the
        form (node, level).
    """
    if lf_nds is None:
        lf_nds = []

    if node.get_children():
        num_of_children = len(node.get_children())
        for i in range(num_of_children):
            collect_leaf_nodes(node=node.get_child(i), lf_nds=lf_nds, level=level + 1)
            logger.debug(f"leaf_nodes so far: {lf_nds}")
            # TODO: Subtraction handling.
            # if (i != num_of_children - 1) and isinstance(node.get_child(i + 1).get_cargo(), defn.Subtract):
            #     result += "-"
            # if (i != num_of_children - 1) and not isinstance(node.get_child(i + 1).get_cargo(), defn.Subtract):
            #     result += str(node.get_cargo())
    else:
        logger.debug(f"appending: '{node, level}'")
        lf_nds.append((node, level))
    logger.debug(f"collect_leaf_nodes returned: {lf_nds}")
    return lf_nds


def get_deepest_leaf_nodes(lf_nds):
    """
    Function to return a list of leaf nodes at the deepest level of the tree.

    :param lf_nds: list of tuples containing a leaf node and its level in the form [(<node>, <level>),].
    :return: list of leaf nodes at the deepest level of the tree.

    :test:
    a = [(1, 2),(3, 1),(18, 75), (6, 14), (89, 75)]
    b = get_deepest_leaf_nodes(a)
    print(b) # should print [(18, 75), (89, 75)]
    """
    depth_level = 0
    deepest_leaf_nodes = []

    for lf in lf_nds:
        if lf[1] == depth_level:
            deepest_leaf_nodes.append(lf[0])
        elif lf[1] > depth_level:
            depth_level = int(lf[1])
            deepest_leaf_nodes.clear()
            deepest_leaf_nodes.append(lf[0])

    return deepest_leaf_nodes


def determine_next_step(lf_nds):
    """
    Function to determine the next step to execute from a list of leaf nodes.

    :param lf_nds: list of leaf nodes expected to come from collect_leaf_nodes.
    :return step_root_node: root node of the next step to be performed
    """
    logger.debug(f"lf_nds = {lf_nds}")
    dp_lf_nds = get_deepest_leaf_nodes(lf_nds)
    logger.debug(f"dp_lf_nds = {dp_lf_nds}")
    still_looking = True
    step_root_node = None
    index = 0
    siblings_found = 0

    while still_looking:
        current_leaf = dp_lf_nds[index]
        siblings = current_leaf.get_parent().get_children()
        logger.debug(f"index: {index}")
        logger.debug(f"current_leaf: {current_leaf}")
        logger.debug(f"siblings: {siblings}")
        for sibling in siblings:
            for lf in dp_lf_nds:
                if id(sibling) == id(lf):  # TODO: use UUID instead of mem address id()
                    siblings_found += 1
                    logger.debug(f"sibling found, siblings_found = {siblings_found}")
                    if siblings_found == len(siblings):
                        step_root_node = current_leaf.get_parent()
                        still_looking = False
        index += 1
    logger.debug(f"step_root_node: {step_root_node} with children: {step_root_node.get_children()}")
    return step_root_node


def evaluate_step(node):
    operation = node.get_cargo()
    operands = tuple(child.get_cargo() for child in node.get_children())
    step_result = operation.execute(operands)
    return step_result


def evaluate_expression(root_node):
    """
    Function to manage the evaluation of the entire expression tree.

    :param root_node: root node of expression tree (or subtree as function recurses)
    :return:
    """
    logger.debug(f"evaluate_expression START ========================================")
    # recursive function's terminating condition; include pointer here for "4 * x" scenario, for example
    if root_node.get_children():

        # Step 0: Raw expression string (happens outside this function)
        # Step 1: Build tree (happens outside this function)

        # Step 2: Collect leaf nodes
        leaf_nodes = collect_leaf_nodes(root_node)

        # Step 3 & 4: Determine next step
        step_node = determine_next_step(leaf_nodes)
        logger.debug(f"The next step is '{step_node}' with children '{step_node.get_children()}'")

        # Step 5: Evaluate the step
        step_result = evaluate_step(step_node)
        logger.debug(f"evaluate_next_step returns {step_result}")

        # Step 6: Update the tree
        focus_node = step_node
        logger.debug(f"focus_node is {focus_node}")
        focus_node.set_cargo(step_result)
        focus_node.clear_all_children()
        logger.debug(f"focus_node is now {focus_node} with children {focus_node.get_children()}")

        logger.debug(f"root_node is {root_node} with children {root_node.get_children()}")
        logger.debug(f"evaluate_expression END ==========================================")

        # Recurse
        evaluate_expression(root_node)

    else:
        return root_node

    return root_node


expr_1 = "1 * 2 + 3 + 4 * 5 * 2"
expr_tree_1 = main.build_tree(expr_1)
print(evaluate_expression(expr_tree_1))


def convert_to_custom_object(raw_input):
    """
    Convert a standard python object (eg. str, int, float) to the appropriate corresponding custom object type
    compatible with this applications tree (eg. Integer, Decimal, Fraction).

    :param raw_input: standard python data type
    :return: appropriate data type defined in definitions.py
    """
    regex_to_class_dict = {
        r"^[0-9]+$": defn.Integer,
        r"^[0-9]+\.[0-9]+$": defn.Decimal,
    }
    converted_input = None
    for pattern in regex_to_class_dict:
        if re.search(pattern, str(raw_input)):
            converted_input = regex_to_class_dict[pattern](raw_input)
    if converted_input is None:
        raise exceptions.FailedToConvertError(raw_input, regex_to_class_dict[pattern])
    logger.debug(f"converted_input: {converted_input} of type {type(converted_input)}")
    return converted_input

