import logging.config
import logging_config.config as lc
import main

# Logging
logging.config.dictConfig(lc.config_dict)
logger = logging.getLogger('my_logger')


# TODO: Am I not supposed to have a default argument be mutable?
def collect_leaf_nodes(node, lf_nds=[], level=0):
    """
    Arguments:
        node: (tree.Node object) to provide starting node from which to begin evaluation.
        lf_nds: (list) to contain the leaf nodes.
        level: (int) to keep track of tree depth level.
    Returns:
        leaf_nodes: (list of tuples) list containing tuples of all leaf nodes and their respective depth level in the
        form (node, level).
    """
    if node.get_children():
        num_of_children = len(node.get_children())
        for i in range(num_of_children):
            collect_leaf_nodes(node=node.get_child(i), level=level + 1)
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
                        logger.debug(f"next_step_root_node: {step_root_node}, "
                                     f"with children: {step_root_node.get_children()}")
                        still_looking = False
        index += 1
    return step_root_node


def evaluate_step(node):
    operation = node.get_cargo()
    operands = tuple(child.get_cargo() for child in node.get_children())
    step_result = operation.execute(operands)
    return step_result


def evaluate_expression(expression):
    """
    Function to manage the evaluation of the entire expression.

    :param str expression: the actual, original expression problem
    :return dict: dictionary of steps
    """
    expr_tree = main.build_tree(expression)
    finished = False

    while not finished:
        leaf_nodes = collect_leaf_nodes(expr_tree)
        step = determine_next_step(leaf_nodes)
        print(f"The next step is '{step}' with children '{step.get_children()}'")
        step_result = evaluate_step(step)
        print(f"evaluate_next_step returns {step_result}")
        finished = True
    return None


expr = "1 + 2 * 3"
evaluate_expression(expr)
