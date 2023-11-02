class Node:
    def __init__(self, value, parent, left_child, right_child):
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return f'value: {self.value}, parent: {self.parent.value}, left: {self.left_child.value}, right: {self.right_child.value}'
