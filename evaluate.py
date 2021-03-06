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


def collect_leaf_nodes(node, lf_nds=None):
    """
    Arguments:
        node: (tree.Node object) to provide starting node from which to begin evaluation.
        lf_nds: (list) to contain the leaf nodes.
    Returns:
        leaf_nodes: (list of tuples) list containing tuples of all leaf nodes and their respective depth level in the
        form (node, level).
    """
    if lf_nds is None:
        lf_nds = []

    # Does node have children?
    if node.get_children():
        num_of_children = len(node.get_children())
        for i in range(num_of_children):
            collect_leaf_nodes(node=node.get_child(i), lf_nds=lf_nds)
            logger.debug(f"leaf_nodes so far: {lf_nds}")
    else:
        logger.debug(f"appending: '{node}'")
        lf_nds.append(node)
    logger.debug(f"collect_leaf_nodes returned: {lf_nds}")
    return lf_nds


def determine_next_step(lf_nds):
    """
    Function to determine the next step to execute from a list of leaf nodes.

    Arguments
        lf_nds: list of leaf nodes expected to come from collect_leaf_nodes
    Return
        candidate_node: root node of the subtree representing the next step to be executed
    """
    logger.debug(f"lf_nds = {lf_nds}")

    order_priority = {
        '*': 0,
        '/': 0,
        '+': 1,
        '-': 1,
    }

    candidate_node = None

    while lf_nds:

        current_leaf = lf_nds[0]
        current_parent = current_leaf.get_parent()
        current_siblings = current_parent.get_children()

        # check if there are any subtractions in current_siblings
        # if yes, then replace each subtraction with it's child
        for i in range(len(current_siblings)):
            if isinstance(current_siblings[i].get_cargo(), defn.Subtract):
                current_siblings[i] = current_siblings[i].get_child()

        if (set(current_siblings) & set(lf_nds)) == set(current_siblings):
            if candidate_node:
                if order_priority[str(current_parent.get_cargo())] < order_priority[str(candidate_node.get_cargo())]:
                    candidate_node = current_parent
            else:
                candidate_node = current_parent

        for sibling in (set(current_siblings) & set(lf_nds)):
            lf_nds.remove(sibling)

    logger.debug(f"returning candidate_node: {candidate_node} with children: {candidate_node.get_children()}")
    return candidate_node


def evaluate_step(node):
    """
    Function to extract the operation and operands from next step subtree and call the appropriate execute function on
    them.

    Arguments
        node: node object which is the subtree root node containing an operation.
    Return
        step_result: whatever the result is of the operation.execute function.
    """
    # get the operation
    operation = node.get_cargo()

    # get the nodes of the operands
    operands_nodes = node.get_children()

    # check if there are any subtractions in the operands nodes
    # if yes, then replace each node containing subtraction with it's child node
    for i in range(len(operands_nodes)):
        if isinstance(operands_nodes[i].get_cargo(), defn.Subtract):
            operands_nodes[i] = operands_nodes[i].get_child()
            reverse_sign_cargo = operands_nodes[i].get_cargo() * -1
            operands_nodes[i].set_cargo(reverse_sign_cargo)

    # list extracted operands
    operands = [operand.get_cargo() for operand in operands_nodes]
    logger.debug(f"operation: {operation}; operands: {operands}")

    # execute the operation on the operands and return the result
    step_result = operation.execute(operands)
    logger.debug(f"step_result: {step_result}")

    # update the tree
    node.set_cargo(step_result)
    node.clear_all_children()

    # return the expression's root node in preparation for recursion
    while node.get_parent():
        node = node.get_parent()

    updated_tree_root_node = node

    return updated_tree_root_node


def evaluate(expr):
    """
    Function to manage the evaluation of an entire expression.

    Arguments
        expr: an expression string in latex form.
    Returns
        root_node: the root (lone) node of the solved expression; should have no children and no parents.
    """
    # 1. build_tree
    root_node = main.build_tree(expr)

    # check if done
    while root_node.get_children():

        # 2. collect_leaf_nodes
        leaf_nodes = collect_leaf_nodes(root_node)

        # 3. determine_next_step
        next_step = determine_next_step(leaf_nodes)

        # 4. evaluate_step
        root_node = evaluate_step(next_step)

    return root_node


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
