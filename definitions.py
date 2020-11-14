"""Operands & Operations defined here."""
import logging.config
import logging_config.config as lc
import main
import tree
import math


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

        numbers = []
        variables = []

        for operand in operands:
            if isinstance(operand, Variable):
                variables.append(operand)
            else:
                numbers.append(operand)

        combined_numbers = str(sum([number.get_value() for number in numbers]))
        combined_variables = " + ".join([variable.get_value() for variable in variables])

        if combined_variables:
            result = combined_variables + "+" + combined_numbers
        else:
            result = combined_numbers
        logger.debug(f"execute returning: {result}")
        return result

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
            result = combined_variables + "*" + combined_numbers
        else:
            result = combined_numbers
        logger.debug(f"execute returning: {result}")
        return result

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
