"""Class definitions for operations and operands."""

import logging.config
import logging_config.config as lc
import main
import tree
import math
import re


# Logging
logging.config.dictConfig(lc.config_dict)
logger = logging.getLogger('info_logger')


class Integer:
    def __init__(self, incoming_latex):
        self.value = int(incoming_latex)

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def grow(self, q_stack):
        # set node to self, pop this node off the q_stack, and return the q_stack
        current_node = q_stack.peek()
        if current_node.get_parent() is None:
            current_node.insert_child(tree.Node(self))
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")
        else:
            current_node.set_cargo(self)
            q_stack.pop()
            current_node = q_stack.peek()
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")
        return q_stack


class Decimal:
    def __init__(self, incoming_latex):
        self.value = float(incoming_latex)

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def get_latex(self):
        return str(self.value)

    def grow(self, q_stack):
        # set node to self, pop this node off the q_stack, and return the q_stack
        current_node = q_stack.peek()
        if current_node.get_parent() is None:
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
        current_node.set_cargo(self)
        q_stack.pop()
        logger.debug(f" - - - - - - ")
        logger.debug(f"      parent: \"{current_node.get_parent()}\"")
        logger.debug(f"current_node: \"{current_node}\"")
        logger.debug(f"    children: \"{current_node.get_children()}\"")
        logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
        logger.debug(f"-------------")
        return q_stack


class Variable:
    def __init__(self, incoming_latex):
        self.value = str(incoming_latex)

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)

    def get_value(self):
        return self.value

    def grow(self, q_stack):
        # set node to self, pop this node off the q_stack, and return the q_stack
        current_node = q_stack.peek()
        if current_node.get_parent() is None:
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
        current_node.set_cargo(self)
        q_stack.pop()
        logger.debug(f" - - - - - - ")
        logger.debug(f"      parent: \"{current_node.get_parent()}\"")
        logger.debug(f"current_node: \"{current_node}\"")
        logger.debug(f"    children: \"{current_node.get_children()}\"")
        logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
        logger.debug(f"-------------")
        return q_stack


class Add:
    def __init__(self, incoming_latex="+"):
        self.latex = incoming_latex

    def __repr__(self):
        return str(self.latex)

    def __str__(self):
        return str(self.latex)

    def execute(self, operands):
        """
        Function to perform addition and subtraction operations on operands. Because of the way the tree is designed to
        construct subtraction (eg. "1 - 2" builds "1 + - 2"), an operand node may actually contain Subtract. To account
        for this, we iterate over the operands and replace their position in the list with their child node if indeed
        they do contain Subtract, multiplying it's cargo by -1. After that, the sum of all the operands is found. If no
        Subtract is found, the sum of all the operands is found.

        Parameters
            :param tuple operands: operands to be multiplied in the form (op_1, op_2, ..., op_n).
        Return
            :return: result; the sum or difference.
        """
        logger.debug(f"operands: {operands} of type {type(operands)}")
        logger.debug(f"operand: {operands[1]} of type {type(operands[1])}")

        res = sum([operand.get_value() for operand in operands])

        logger.debug(f"execute returning: {res}")
        return res

    def grow(self, q_stack):
        current_node = q_stack.peek()

        if not current_node.get_cargo():
            # set current node cargo to self, add a child, and go to it
            current_node.set_cargo(self)
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")

        elif isinstance(current_node.get_cargo(), Add):
            # add a child and go to it
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")

        elif isinstance(current_node.get_cargo(), Subtract):
            # move to parent, add a child, and go to it
            q_stack.pop()
            current_node = q_stack.peek()
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")

        elif isinstance(current_node.get_cargo(), Multiply) or isinstance(current_node.get_cargo(), Divide):
            # first check if parent exists, go to the parent, create a child, and go to it
            if current_node.get_parent() is None:
                parent = tree.Node(self)
                current_node.set_parent(parent)
                q_stack.reset(parent)
                q_stack.push(current_node)
            if isinstance(current_node.get_parent().get_cargo(), Subtract):
                current_node = current_node.get_parent()
                q_stack.pop()
            current_node = current_node.get_parent()
            q_stack.pop()
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")


class Subtract:
    def __init__(self, incoming_latex):
        self.latex = incoming_latex

    def __repr__(self):
        return str(self.latex)

    def __str__(self):
        return str(self.latex)

    def execute(self):
        pass

    def grow(self, q_stack):
        current_node = q_stack.peek()

        if not current_node.get_cargo():
            # set current node to "+", create child with "-", create a child of minus, and go to it
            current_node.set_cargo(Add())
            q_stack.reset(current_node)
            current_node.insert_child(tree.Node(self))
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f"current node is \"{current_node}\" with parent \"{current_node.get_parent()}\" "
                         f"and children \"{current_node.get_children()}\"")
            logger.debug(f"stack: {q_stack.get_full_stack()}")

        elif isinstance(current_node.get_cargo(), Add):
            # create child with "-" and go to it, create a child of minus and go to it
            current_node.insert_child(tree.Node(self))
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f"current node is \"{current_node}\" with parent \"{current_node.get_parent()}\" "
                         f"and children \"{current_node.get_children()}\"")
            logger.debug(f"stack: {q_stack.get_full_stack()}")

        elif isinstance(current_node.get_cargo(), Subtract):
            # go to parent, create child with "-" and go to it, create child of minus and go to it
            q_stack.pop()
            current_node = q_stack.peek()
            current_node.insert_child(tree.Node(self))
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f"current node is \"{current_node}\" with parent \"{current_node.get_parent()}\" "
                         f"and children \"{current_node.get_children()}\"")
            logger.debug(f"stack: {q_stack.get_full_stack()}")

        elif isinstance(current_node.get_cargo(), Multiply):
            # first check if parent exists, go to the parent, create a child, and go to it
            if current_node.get_parent() is None:
                parent = tree.Node(Add())
                current_node.set_parent(parent)
                q_stack.reset(parent)
                q_stack.push(current_node)
                current_node = current_node.get_parent()
                q_stack.pop()
                current_node.insert_child(tree.Node(self))
                current_node = current_node.get_child(index=-1)
                q_stack.push(current_node)
                current_node.insert_child(tree.Node())
                current_node = current_node.get_child(index=-1)
                q_stack.push(current_node)
                logger.debug(f"current node is \"{current_node}\" with parent \"{current_node.get_parent()}\" "
                             f"and children \"{current_node.get_children()}\"")
                logger.debug(f"stack: {q_stack.get_full_stack()}")

            elif isinstance(current_node.get_parent().get_cargo(), Subtract):
                current_node = current_node.get_parent()
                q_stack.pop()
                current_node = current_node.get_parent()
                q_stack.pop()
                current_node.insert_child(tree.Node(self))
                current_node = current_node.get_child(index=-1)
                q_stack.push(current_node)
                current_node.insert_child(tree.Node())
                current_node = current_node.get_child(index=-1)
                q_stack.push(current_node)
                logger.debug(f"current node is \"{current_node}\" with parent \"{current_node.get_parent()}\" "
                             f"and children \"{current_node.get_children()}\"")
                logger.debug(f"stack: {q_stack.get_full_stack()}")

            else:
                current_node = current_node.get_parent()
                q_stack.pop()
                current_node.insert_child(tree.Node(self))
                current_node = current_node.get_child(index=-1)
                q_stack.push(current_node)
                current_node.insert_child(tree.Node())
                current_node = current_node.get_child(index=-1)
                q_stack.push(current_node)
                logger.debug(f"current node is \"{current_node}\" with parent \"{current_node.get_parent()}\" "
                             f"and children \"{current_node.get_children()}\"")
                logger.debug(f"stack: {q_stack.get_full_stack()}")

        elif isinstance(current_node.get_cargo(), Divide):
            # first check if parent exists, go to the parent, create a child, and go to it
            if current_node.get_parent() is None:
                parent = tree.Node(Add())
                current_node.set_parent(parent)
                q_stack.reset(parent)
                q_stack.push(current_node)
                current_node = current_node.get_parent()
                q_stack.pop()
                current_node.insert_child(tree.Node(self))
                current_node = current_node.get_child(index=-1)
                q_stack.push(current_node)
                current_node.insert_child(tree.Node())
                current_node = current_node.get_child(index=-1)
                q_stack.push(current_node)
                logger.debug(f"current node is \"{current_node}\" with parent \"{current_node.get_parent()}\" "
                             f"and children \"{current_node.get_children()}\"")
                logger.debug(f"stack: {q_stack.get_full_stack()}")

            elif isinstance(current_node.get_parent().get_cargo(), Subtract):
                current_node = current_node.get_parent()
                q_stack.pop()
                current_node = current_node.get_parent()
                q_stack.pop()
                current_node.insert_child(tree.Node(self))
                current_node = current_node.get_child(index=-1)
                q_stack.push(current_node)
                current_node.insert_child(tree.Node())
                current_node = current_node.get_child(index=-1)
                q_stack.push(current_node)
                logger.debug(f"current node is \"{current_node}\" with parent \"{current_node.get_parent()}\" "
                             f"and children \"{current_node.get_children()}\"")
                logger.debug(f"stack: {q_stack.get_full_stack()}")

            else:
                current_node = current_node.get_parent()
                q_stack.pop()
                current_node.insert_child(tree.Node(self))
                current_node = current_node.get_child(index=-1)
                q_stack.push(current_node)
                current_node.insert_child(tree.Node())
                current_node = current_node.get_child(index=-1)
                q_stack.push(current_node)
                logger.debug(f"current node is \"{current_node}\" with parent \"{current_node.get_parent()}\" "
                             f"and children \"{current_node.get_children()}\"")
                logger.debug(f"stack: {q_stack.get_full_stack()}")


class Multiply:
    def __init__(self, incoming_latex="*"):
        self.latex = incoming_latex

    def __repr__(self):
        return str(self.latex)

    def __str__(self):
        return str(self.latex)

    def execute(self, operands):
        """
        Function to perform multiplication operation on operands.

        :param tuple operands: operands to be multiplied in the form (<op_1>, <op_2>, ..., <op_n>)
        :return: result
        """

        """
        This execute function is responsible for determining the output of the multiply operation on whatever operands
        are passed to it.
            - if there can be no operation performed (eg. "2 * x"), return "no change" and evaluate_expression function
                picks up from there because it's keeping a pointer on the root node of that subtree (in this case, *) 
                and collect_leaf_nodes will treat that node as a leaf node on the next traversal 
            - if there can be an operation performed, (eg. "2 * 3"), return the result as a value of the correct type of 
                the result (in this case, Integer(6))
        """
        numbers = []
        variables = []

        for operand in operands:
            if isinstance(operand, Variable):
                variables.append(operand)
            else:
                numbers.append(operand)

        combined_numbers = str(math.prod([number.get_value() for number in numbers]))
        combined_variables = " * ".join([variable.get_value() for variable in variables])

        if combined_variables:
            raw_result = combined_variables + "*" + combined_numbers
        else:
            raw_result = combined_numbers

        logger.debug(f"raw_result: {raw_result} of type {type(raw_result)}")

        # TODO: write a function to create the proper type of result object based on what result is. This function
        # TODO: needs to be callable from all 'execute' functions.

        # convert raw_result to a usable type
        regex_to_class_dict = {
            r"^[0-9]+$": Integer,
            r"^[0-9]+\.[0-9]+$": Decimal,
        }
        typed_result = None
        for pattern in regex_to_class_dict:
            if re.search(pattern, raw_result):
                typed_result = regex_to_class_dict[pattern](raw_result)
        logger.debug(f"typed_result: {typed_result} of type {type(typed_result)}")
        return typed_result

    def grow(self, q_stack):
        current_node = q_stack.peek()

        if not current_node.get_cargo():
            # set current node cargo to self, add a child, and go to it
            current_node.set_cargo(self)
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")

        elif isinstance(current_node.get_cargo(), Add):
            # go to last child, create a child with cargo of current node, set the current node to self, create a
            # child, and go to it
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            current_node.insert_child(tree.Node(current_node.get_cargo()))
            current_node.set_cargo(self)
            q_stack.pop()
            q_stack.push(current_node)
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")

        elif isinstance(current_node.get_cargo(), Subtract):
            # go to last child, create a child with cargo of current node, set the current node to self, create a
            # child, and go to it
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            current_node.insert_child(tree.Node(current_node.get_cargo()))
            current_node.set_cargo(self)
            q_stack.pop()
            q_stack.push(current_node)
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")

        elif isinstance(current_node.get_cargo(), Multiply):
            # set current node cargo to i, add a child, and go to it
            current_node.set_cargo(self)
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")

        elif isinstance(current_node.get_cargo(), Divide):
            new_node = tree.Node(self)
            if current_node.get_parent() is not None:
                current_node.get_parent().remove_child()
                current_node.get_parent().insert_child(new_node)
            current_node.set_parent(new_node)
            new_node.insert_child(current_node)
            new_node.remove_child(index=-1)
            current_node = new_node
            q_stack.pop()
            q_stack.push(current_node)
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")


class Divide:
    def __init__(self, incoming_latex):
        self.latex = incoming_latex

    def __repr__(self):
        return str(self.latex)

    def __str__(self):
        return str(self.latex)

    def execute(self, operands):
        """
        Function to perform division operation. Only capable of returning decimals in the form of standard
        floats currently.
        Parameters
            operands (tuple): operands in the form (dividend, divisor).
        Return
            res (float): the quotient resulting from dividing the dividend by the divisor.
        """
        dividend = operands[0].get_value()
        divisor = operands[1].get_value()
        quotient = dividend / divisor
        logger.debug(f"quotient: {quotient}, type:{type(quotient)}")

        res = Decimal(quotient)
        return res

    def grow(self, q_stack):
        current_node = q_stack.peek()

        if not current_node.get_cargo():
            # set current node cargo to self, add a child, and go to it
            current_node.set_cargo(self)
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")

        elif isinstance(current_node.get_cargo(), Add):
            # go to last child, create a child with cargo of current node, set the current node to self, create a
            # child, and go to it
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            current_node.insert_child(tree.Node(current_node.get_cargo()))
            current_node.set_cargo(self)
            q_stack.pop()
            q_stack.push(current_node)
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")

        elif isinstance(current_node.get_cargo(), Subtract):
            # go to last child, create a child with cargo of current node, set the current node to i, create a
            # child, and go to it
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            current_node.insert_child(tree.Node(current_node.get_cargo()))
            current_node.set_cargo(self)
            q_stack.pop()
            q_stack.push(current_node)
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")

        elif isinstance(current_node.get_cargo(), Multiply):
            # exact same as below
            new_node = tree.Node(self)
            if current_node.get_parent() is not None:
                current_node.get_parent().remove_child()
                current_node.get_parent().insert_child(new_node)
            current_node.set_parent(new_node)
            new_node.insert_child(current_node)
            new_node.remove_child(index=-1)
            current_node = new_node
            q_stack.pop()
            q_stack.push(current_node)
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")

        elif isinstance(current_node.get_cargo(), Divide):
            # exact same as above
            new_node = tree.Node(self)
            if current_node.get_parent() is not None:
                current_node.get_parent().remove_child()
                current_node.get_parent().insert_child(new_node)
            current_node.set_parent(new_node)
            new_node.insert_child(current_node)
            new_node.remove_child(index=-1)
            current_node = new_node
            q_stack.pop()
            q_stack.push(current_node)
            current_node.insert_child(tree.Node())
            current_node = current_node.get_child(index=-1)
            q_stack.push(current_node)
            logger.debug(f" - - - - - - ")
            logger.debug(f"      parent: \"{current_node.get_parent()}\"")
            logger.debug(f"current_node: \"{current_node}\"")
            logger.debug(f"    children: \"{current_node.get_children()}\"")
            logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
            logger.debug(f"-------------")


class Power:
    def __init__(self, incoming_latex):
        counter = 0
        res = []

        for i, char in enumerate(incoming_latex):
            if char == '{':
                counter += 1
            elif char == '}':
                counter += -1
            if counter == 0:
                res.append((i, char))

        if len(res) == 3 and res[1][1] == '^':
            base = incoming_latex[1:res[0][0]]
            exponent = incoming_latex[(res[1][0] + 2):res[2][0]]
            self.base = main.build_tree(base)
            self.exponent = main.build_tree(exponent)

    def __repr__(self):
        return f"power with base: {self.base}, exponent: {self.exponent}"

    def __str__(self):
        return f"{self.base}^{self.exponent}"

    def grow(self, q_stack):
        # set node to self (Power), create and set children for base and exponent,
        # pop this node off the q_stack (aka go to parent, basically), and return the q_stack
        current_node = q_stack.peek()
        current_node.set_cargo(self)
        current_node.insert_child(tree.Node(self.base))
        current_node.insert_child(tree.Node(self.exponent))
        q_stack.pop()
        logger.debug(f" - - - - ")
        logger.debug(f"      parent: \"{current_node.get_parent()}\"")
        logger.debug(f"current_node: \"{current_node}\"")
        logger.debug(f"    children: \"{current_node.get_children()}\"")
        logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
        logger.debug(f"-------------")
        return q_stack


class Fraction:
    def __init__(self, incoming_latex):
        counter = 0
        res = []
        modified_latex = incoming_latex[5:]

        for i, char in enumerate(modified_latex):
            if char == '{':
                counter += 1
            elif char == '}':
                counter += -1
            if counter == 0:
                res.append((i, char))

        if len(res) == 2 and res[1][1] == '}':
            numerator = modified_latex[1:res[0][0]]
            denominator = modified_latex[(res[0][0] + 2):-1]
            self.numerator = main.build_tree(numerator)
            self.denominator = main.build_tree(denominator)

    def __repr__(self):
        return f"fraction with numerator: {self.numerator}, denominator: {self.denominator}"

    def __str__(self):
        return f"fraction with numerator: {self.numerator}, denominator: {self.denominator}"

    def grow(self, q_stack):
        # set node to self (fraction), create and set children for numerator and denominator,
        # pop this node off the q_stack (aka go to parent, basically), and return the q_stack
        current_node = q_stack.peek()
        current_node.set_cargo(self)
        current_node.insert_child(tree.Node(self.numerator))
        current_node.insert_child(tree.Node(self.denominator))
        q_stack.pop()
        logger.debug(f" - - - - ")
        logger.debug(f"      parent: \"{current_node.get_parent()}\"")
        logger.debug(f"current_node: \"{current_node}\"")
        logger.debug(f"    children: \"{current_node.get_children()}\"")
        logger.debug(f"     p_stack: {q_stack.get_full_stack()}")
        logger.debug(f"-------------")
        return q_stack


class Logarithm:
    def __init__(self, incoming_latex):
        counter = 0
        res = []
        modified_latex = incoming_latex[5:]

        for i, char in enumerate(modified_latex):
            if char == '{':
                counter += 1
            elif char == '}':
                counter += -1
            if counter == 0:
                res.append((i, char))

        if len(res) == 2 and res[1][1] == '}':
            base = modified_latex[1:res[0][0]]
            anti_log = modified_latex[(res[0][0] + 2):-1]
            self.base = main.build_tree(base)
            self.anti_log = main.build_tree(anti_log)

    def __repr__(self):
        return f"logarithm with base: {self.base}, anti_log: {self.anti_log}"

    def __str__(self):
        return f"logarithm with base: {self.base}, anti_log: {self.anti_log}"


class SquareRoot:
    def __init__(self, incoming_latex):
        counter = 0
        res = []
        modified_latex = incoming_latex[5:]

        for i, char in enumerate(modified_latex):
            if char == '[':
                counter += 1
            elif char == ']':
                counter += -1
            if counter == 0:
                res.append((i, char))
                break

        index = modified_latex[1:res[0][0]]
        radicand = modified_latex[(res[0][0] + 2):-1]
        self.index = main.build_tree(index)
        self.radicand = main.build_tree(radicand)

    def __repr__(self):
        return f"square root with index: {self.index}, radicand: {self.radicand}"

    def __str__(self):
        return f"square root with index: {self.index}, radicand: {self.radicand}"

    def grow(self):
        pass
