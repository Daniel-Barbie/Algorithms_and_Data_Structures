class LinkedList():

    def __init__(self, head=None):
        self.head = head

    # inefficient, needs refactoring:
    def __repr__(self):
        elements = []
        current_node = self.head
        while current_node:
            elements.append(current_node.data)
            current_node = current_node.pointer
        return_string = ""
        for i in elements:
            return_string += "{}, ".format(i)
        return_string += "STOP"
        return return_string

    def insert(self, key, data):
        current_node = self.head
        next_node = self.head.pointer
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
            new_top_node = Node(data)
            new_top_node.pointer = self.head
            self.head = new_top_node
            return True
        self.head = Node(data)

    def insert_bottom(self, data):
        current_node = self.head
        next_node = self.head.pointer
        while next_node is not None:
            current_node = next_node
            next_node = current_node.pointer
        current_node.pointer = Node(data)
        return True

    def delete(self, key):
        last_node = None
        current_node = self.head
        next_node = self.head.pointer
        while current_node.data != key:
            if next_node is None:
                return False
            last_node = current_node
            current_node = next_node
            next_node = current_node.pointer
        if last_node is None:
            self.head = current_node.pointer
        else:
            last_node.pointer = next_node
        del current_node
        return True


class Node():

    def __init__(self, data):
        self.data = data
        self.pointer = None
        self.head = False


# test it out!

ll = LinkedList(Node(1))
print(ll)
ll.insert(1, 2)
print(ll)
ll.insert(2, 3)
print(ll)
ll.insert(2, 4)
print(ll)
ll.insert(1, 5)
print(ll)
ll.insert_top(10)
print(ll)
ll.insert_bottom(20)
print(ll)
ll.delete(10)
print(ll)