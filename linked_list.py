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


ll = create_ll(5)
print(ll)
# list_ = [[1,"A"], [2,"B"], [3,"C"], [4,"D"], [5,"E"]]
# create_linked_list(list_)

elements_to_insert = [DataObject(2, "X"),
                      DataObject(4, "Y"),
                      DataObject(3.5, "3.5"),
                      DataObject(1, "one")]
for i in elements_to_insert:
    ll.insert(i.key, i.data)
print(ll)
