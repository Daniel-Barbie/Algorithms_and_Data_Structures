import time
import random
import matplotlib.pyplot as plt


class Node():

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.right = None
        self.left = None

    def get(self, key):
        if self.key == key:
            return self.data
        elif self.key < key and self.right is not None:
            return self.right.get(key)
        elif self.key > key and self.left is not None:
            return self.left.get(key)
        else:
            return None

    def insert(self, key, data):
        if self.key == key:
            self.data = data
            # self.data = Node(key, data)

        elif self.key < key:
            if self.right is None:
                self.right = Node(key, data)
            else:
                self.right.insert(key, data)

        elif self.key > key:
            if self.left is None:
                self.left = Node(key, data)
            else:
                self.left.insert(key, data)

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


    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

# constructing the tree from a sorted list
def construct_bst(list_, top_node=None):
    if top_node is None:
        top_node = Node(list_[len(list_) // 2].key, list_[len(list_) // 2])

    middle = len(list_) // 2

    if len(list_) > 1:
        list_1 = list_[:middle]
        top_node.insert(list_1[len(list_1) // 2].key, list_1[len(list_1) // 2])
        top_node = construct_bst(list_1, top_node)

        if len(list_) > 2:
            list_2 = list_[middle + 1:]
            top_node.insert(list_2[len(list_2) // 2].key, list_2[len(list_2) // 2])
            construct_bst(list_2, top_node)

    return top_node


# TIME COMPLEXITY

# dummy DataObject with attributes 'key' and 'data'
class DataObject:

    def __init__(self, key, data):
        self.key = key
        self.data = data


# return time-complexity for a tree of 'n' objects with 'k' sampled keys to apply 'get' with
def test_bst_time_complexity(n, k):
    a = 1
    objectlist = []
    while a <= n:
        objectlist.append(DataObject(a, str(a)))
        a += 1
    start = time.time()
    bst = construct_bst(objectlist)
    end = time.time()
    print("Tree creation took {} seconds.".format(end-start))
    samplelist = random.sample(objectlist, k)
    start = time.time_ns()
    for i in samplelist:
        bst.get(i.key)
    end = time.time_ns()
    seconds = end-start
    return seconds


def create_bst(n):
    a = 1
    objectlist = []
    while a <= n:
        objectlist.append(DataObject(a, str(a)))
        a += 1
    bst = construct_bst(objectlist)
    return bst


# test tree creation & display
bst = create_bst(100)
print("Test the binary search tree creation:")
bst.display()

# different tree sizes
reps_list = [1000000, 2000000, 4000000, 8000000]

time_complexity_results = []

# get time complexity for tree sizes in reps_list
for i in reps_list:
    time_complexity_results.append(test_bst_time_complexity(i,1000))
    print(time_complexity_results)

# get average time complexity for a single 'get' call per tree size of 'reps_list'
time_complexity_results_1 = []
for i in time_complexity_results:
    time_complexity_results_1.append(i/1000)

# plot all the time complexities
plt.plot(reps_list, time_complexity_results_1)
plt.show()
