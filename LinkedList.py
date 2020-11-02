class Node():

    def __init__(self, data):
        self.data = data
        self.pointer = None
        self.head = False

    # inefficient, needs refactoring:
    def __repr__(self):
        elements = []
        current_node = self
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.pointer
        return_string = ""
        for i in elements:
            return_string += "{}, ".format(i)
        return_string += "STOP"
        return return_string

    def set_head(self):
        self.head = True

    def insert(self, key, data):
        current_node = self
        next_node = self.pointer
        while current_node.data != key:
            if next_node is None:
                return False
            current_node = current_node.pointer
            next_node = current_node.pointer
        if next_node is None:
            current_node.pointer = Node(data)
            return True
        old_pointer = current_node.pointer
        current_node.pointer = Node(data)
        current_node.pointer.pointer = old_pointer
        return True

    def insert_top(self, data):
        if self.head:
            old_top_node = Node(self.data)
            old_top_node.pointer = self.pointer
            self.pointer = old_top_node
            return True

    def insert_bottom(self, data):
        current_node = self
        next_node = self.pointer
        while next_node is not None:
            current_node = next_node
            next_node = current_node.pointer
        current_node.pointer = Node(data)
        return True

    def delete(self, key):
        last_node = None
        current_node = self
        next_node = self.pointer
        while current_node.data != key:
            if next_node is None:
                return False
            last_node = current_node
            current_node = next_node
            next_node = current_node.pointer
        last_node.pointer = next_node
        del current_node
        return True


# test it out!

ll = Node(1)
ll.set_head()
print(ll)
ll.insert(1, 2)
print(ll)
ll.insert(2, 3)
print(ll)
ll.insert(2, 4)
print(ll)
ll.insert(1, 5)
print(ll)


