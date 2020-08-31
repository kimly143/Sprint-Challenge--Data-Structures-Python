class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    # def reverse_list(self, node, prev):
    def reverse_list(self, arg1, arg2):
        # base case, node as of current node is None
        # this is not double linkedlist so we do not have previous node info
        # so the return value would be prev node       
        if arg1 is None:
            self.head = arg2
            return arg2
        # if arg1 is not None
        # a transition node store the return value of the reverse_list call for next of arg1 and set arg1 as "arg2" in the input
        # arg1.next_node is arg1 in reverse list call
        # arg1 is now arg2 is reverse list call

        transition_node = self.reverse_list(arg1.get_next(), arg1)
        # next node of transition_node is now arg2
        transition_node.set_next(arg2)
        return arg2
