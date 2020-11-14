"""Node and Stack classes are defined here."""
import logging.config
import logging_config.config as lc


# Logging
logging.config.dictConfig(lc.config_dict)
logger = logging.getLogger('my_logger')


class Node:
    def __init__(self, cargo=None):
        self.cargo = cargo
        self.parent = None
        self.children = []

    def __repr__(self):
        return str(self.cargo)

    def set_cargo(self, cargo):
        self.cargo = cargo

    def get_cargo(self):
        return self.cargo

    def set_parent(self, parent):
        # verify parent is a Node object, make the two way child-parent connection, and reflect this in the stack
        if isinstance(parent, Node):
            self.parent = parent
            parent.children.append(self)
        else:
            err_needs_node_obj = TypeError(f"Tried to insert \"{parent}\" {type(parent)} as a parent. "
                                           f"Can only insert Node objects.")
            raise err_needs_node_obj

    def get_parent(self):
        """Returns the parent, which should be either None or a Node object."""
        return self.parent

    def insert_child(self, child):
        # verify child is a Node object, make the two way child-parent connection, and reflect this in the stack
        if isinstance(child, Node):
            self.children.append(child)
            child.parent = self
        else:
            err_needs_node_obj = TypeError(f"Tried to insert \"{child}\" {type(child)} as a child. "
                                           f"Can only insert Node objects.")
            raise err_needs_node_obj

    def get_child(self, index=-1):
        """Returns a child as a Node object."""
        return self.children[index]

    def get_children(self):
        """Returns a list of children as Node objects."""
        return [i for i in self.children]

    def remove_child(self, index=-1):
        """Remove all of the node's children."""
        self.children.pop(index)

    def go_to(self, destination_node):
        pass


class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not bool(self._items)

    def push(self, node):
        self._items.append(node)
        # if isinstance(node, Node):
        #     self._items.append(node)
        # else:
        #     err_needs_node_obj = TypeError(f"Tried to push \"{node}\" {type(node)} to the stack. "
        #                                 f"Can only push Node objects.")
        #     raise err_needs_node_obj

    def pop(self, index=-1):
        return self._items.pop(index)

    def peek(self, index=-1):
        return self._items[index]

    def size(self):
        return len(self._items)

    def get_full_stack(self):
        """ For readability only. Returns all elements of the stack as a list of strings. Use push(), pop(), and peek()
        methods for navigation."""
        return [node.get_cargo() for node in self._items]

    def reset(self, node):
        self._items = [node]
