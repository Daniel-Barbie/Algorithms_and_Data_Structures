# This is the insertion sorting algorithm coded by Daniel Barbie
# 1st Individual Assignment of Algorithms & Data Structures
# MSc Applied Data Science @ Frankfurt School
# Class of 2022

# created using PyCharm

def insertion_sort(element_list):
    # start at the second element
    j = 1
    # go on until every element has been checked
    while j < len(element_list):
        # 'key' is the element to be sorted
        key = element_list[j]
        # compare with the element at (position of key) - 1
        i = j-1
        # check until beginning of the list has been reached or a smaller element has been reached
        while i >= 0 and element_list[i] > key:
            # up the position of the element to compare to & go to a position that is lower by 1
            element_list[i+1] = element_list[i]
            i = i-1
        # place 'key' in the right position
        element_list[i+1] = key
        # take the next element in the list as 'key'
        j = j+1
    return element_list
