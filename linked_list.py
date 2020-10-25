import time
import random
import matplotlib.pyplot as plt


class Node():

    def __init__(self, key, data, pointer=None):
        self.key = key
        self.data = data
        self.pointer = pointer

    def __repr__(self):
        list_ = [self.get(self.key)]
        pointer = self.pointer
        while pointer.pointer is not None:
            list_.append(pointer.get(pointer.key))
            pointer = pointer.pointer
        list_.append(pointer.get(pointer.key))
        return str(list_)

    def get(self, key):
        if self.key == key:
            return self.data
        elif self.pointer is None:
            return False
        else:
            return self.pointer.get(key)

    def insert(self, key, data):
        if self.key == key:
            self.data = data

        elif self.key > key:
            new_node = Node(self.key, self.data, self.pointer)
            self.pointer = new_node
            self.key = key
            self.data = data

        elif self.pointer is None:
            self.pointer = Node(key, data)

        else:
            self.pointer.insert(key, data)


def construct_ll(list_, root_element=None):
    if root_element is None:
        root_element = Node(list_[0].key, list_[0].data)
    #list_ = list_[1:]
    for i in list_[1:]:
        root_element.insert(i.key, i.data)
    return root_element


# dummy DataObject with attributes 'key' and 'data'
class DataObject:

    def __init__(self, key, data):
        self.key = key
        self.data = data


def create_ll(n):
    a = 1
    objectlist = []
    while a <= n:
        objectlist.append(DataObject(a, str(a)))
        a += 1
    ll = construct_ll(objectlist)
    return ll


# return time-complexity for a tree of 'n' objects with 'k' sampled keys to apply 'get' with
#def test_ll_time_complexity(node, n):
#    start = time.time()
#    for i in range(n):
#        node.insert()
#    end = time.time()
#    print("Tree creation took {} seconds.".format(end-start))
#    samplelist = random.sample(objectlist, k)
#    start = time.time_ns()
#    for i in samplelist:
#        bst.get(i.key)
#    end = time.time_ns()
#    seconds = end-start
#    return seconds


# create initial ll with 5 Nodes
ll = create_ll(5)
print(ll)

# define elements to insert for testing
elements_to_insert = [DataObject(2, "X"),
                      DataObject(4, "Y"),
                      DataObject(3.5, "3.5"),
                      DataObject(1, "one")]
# insert elements
for i in elements_to_insert:
    ll.insert(i.key, i.data)
print(ll)

reps_list = [1000000, 2000000, 4000000, 8000000]
time_complexity_results = []

for i in reps_list:
    start = time.time_ns()
    for j in range(i):
        curr_element_to_insert = elements_to_insert[j % 4]
        ll.insert(curr_element_to_insert.key, curr_element_to_insert.data)
    end = time.time_ns()
    time_complexity_results.append(end-start)


# # get time complexity for tree sizes in reps_list
# for i in reps_list:
#     for j in range(i):
#         time_complexity_results.append(test_ll_time_complexity(i, 1000))
#     print(time_complexity_results)
#
# # get average time complexity for a single 'get' call per tree size of 'reps_list'
# time_complexity_results_1 = []
# for i in time_complexity_results:
#     time_complexity_results_1.append(i/1000)

print(reps_list, time_complexity_results)
# plot all the time complexities
plt.plot(reps_list, time_complexity_results)
ax = plt.gca()
ax.get_xaxis().get_major_formatter().set_useOffset(False)
plt.show()
