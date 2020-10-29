# Option 2:
# algorithm description:
# We start by comparing every element of the first list with every element of the second list. The first element of
# list 1 is compared with every element of list 2 until the end of list 2 is reached or until the current element of list 2
# is bigger than our element from list 1. When either case happens, we take the next element of list 1 and do the same operation.
# If the end of list 1 is reached without finding a match in numbers, the process will end and it will return -1.
# Now if a match is found in two consecutive lists, it is checked whether the next list also containes the element. This is being
# done recursively until either the last list of the list contains the same element or until one list does not contain the element.
# In the first case, which is, that every list including the last list contains the element, the process will end and subsequently return the
# specified element. If the second case is reached, that is, one of the lists does not contain the element we are looking for,
# then the recursion will stop and signal that no match was found. The recursive call will stop altogether and the next element of the first list
# will be compared as described above. The time complexity will be O(n^2) in the worst case.


def find_smallest_common_element(mat, element=None, k=None):
    if k is None:
        k = True
    print("list of lists: {}".format(mat))
    current_list = mat[0]
    print("current list: {}, element given: {}".format(mat[0], element))
    for i in current_list:
        if k:
            print("initial setup")
            element = i
            element = current_list[i]
            if find_smallest_common_element(mat[1:], element, False) != -1:
                return element
        else:
            if i == element:
                print("match! element {} in list {}".format(i, current_list))
                if len(mat) <= 1:
                    print("reached end of lists! returning element {}".format(element))
                    return element
                else:
                    print("check next list {} for element {}".format(mat[1], element))
                    return find_smallest_common_element(mat[1:], element, False)
            elif i > element:
                print("found bigger number, stopping recursion in list {} with element {}".format(current_list, element))
                return -1
    return -1





mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
print(find_smallest_common_element(mat))