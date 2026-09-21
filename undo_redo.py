from node import Node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        if self.top is None:
            return None

        return self.top.value

    def print_stack(self):
        current = self.top
        while current is not None:
            print(current.value)
            current = current.next
