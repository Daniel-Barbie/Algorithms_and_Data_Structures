# 3 Recursive Functions
#
# 1. insert into a list
# 2. get from the list
# 3. take sorted list & create balanced binary search tree

# class Node:
# __init__()

# binary search tree
# time complexity for insert value
# time complexity for get value (only important for assignment)
# search for random element 100times and average the time complexity
# for n > 1 mio

class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

    def insert(self, key, data):
        if self.key > key:
            if self.left is None:
                self.left = Node(key, data)
            else:
                self.left.insert(key, data)
        elif self.key < key:
            if self.right is None:
                self.right = Node(key, data)
            else:
                self.right.insert(key, data)
        elif self.key == key:
            self.data = data

    def get(self, key):
        if self.key == key:
            return self.data
        elif self.key > key:
            return self.left.get(key)
        elif self.key < key:
            return self.right.get(key)
        else:
            print("Key does not exist")
            return None

    # --------------------------------

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# ————————————

class DataObject():

    def __init__(self, key, data):
        self.key = key
        self.data = data


a = 1
objectlist = []
while a < 40:
    objectlist.append(DataObject(a, str(a)))
    a += 1


def construct(list_, node=None):
    if node is None:
        node = Node(list_[len(list_) // 2].key, list_[len(list_) // 2].data)

    middle = len(list_) // 2

    if len(list_) > 1:
        left = list_[:middle]
        node.insert(left[len(left) // 2].key, left[len(left) // 2].data)
        construct(left, node)

    if len(list_) > 2:
        right = list_[middle + 1:]
        node.insert(right[len(right) // 2].key, right[len(right) // 2].data)
        construct(right, node)

    return node

