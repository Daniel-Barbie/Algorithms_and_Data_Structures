class LinkedList():

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.pointer = None

    def __repr__(self):
        str_1 = self.get(str(self.key))
        #str_1 = str_1 + str(self.pointer.get())
        return "__repr__ to be implemented..."

    def get(self, key):
        if self.key == key:
            return self.data
        elif self.pointer is None:
            return "end of list"
        else:
            return self.pointer.get(key)

    def insert(self, key, data):
        if self.key == key:
            self.data = data

        # elif self.pointer.key > key:
        #    old_pointer = self.pointer
        #    self.pointer = LinkedList(key, data)
        #    self.pointer.insert(old_pointer)

        elif self.key > key:
            self.pointer = self
            self.key = key
            self.data = data

        elif self.pointer is None:
            self.pointer = LinkedList(key, data)

        else:
            self.pointer.insert(key, data)


def construct_ll(list_, root_element=None):
    if root_element is None:
        root_element = LinkedList(list_[0].key, list_[0].data)
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
print(ll.key)
print(ll)
# list_ = [[1,"A"], [2,"B"], [3,"C"], [4,"D"], [5,"E"]]
# create_linked_list(list_)
