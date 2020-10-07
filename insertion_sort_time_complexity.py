# group members: Lais Lima, Tom Schult, Nico Bambach, Georg Schafft
# this assignment is my individual code, it is not our group code

import matplotlib.pyplot as plt
import timeit
import random


# define insertion sort algorithm
def insertion_sort(element_list):
    # start at the second element
    j = 1
    # go on until every element has been checked
    while j < len(element_list):
        # 'key' is the element to be sorted
        key = element_list[j]
        # compare with the element at (position of key) - 1
        i = j - 1
        # check until beginning of the list has been reached or a smaller element has been reached
        while i >= 0 and element_list[i] > key:
            # up the position of the element to compare to & go to a position that is lower by 1
            element_list[i + 1] = element_list[i]
            i = i - 1
        # place 'key' in the right position
        element_list[i + 1] = key
        # take the next element in the list as 'key'
        j = j + 1
    return element_list


def create_best_case(number):
    list_ = list(range(0, number))
    return list_


def create_worst_case(number):
    list_ = list(range(0, number))
    list_.reverse()
    return list_


def create_average_case(number):
    list_ = list(range(0, number))
    random.shuffle(list_)
    return list_


result_array_best = list()
result_array_worst = list()
result_array_average = list()

# setup code to run timeit.timeit with best case
best_case_setup = """
from __main__ import create_best_case, insertion_sort
best_case_list = create_best_case({0})"""

# setup code to run timeit.timeit with worst case
worst_case_setup = """
from __main__ import create_worst_case, insertion_sort
worst_case_list = create_worst_case({0})"""

# setup code to run timeit.timeit with average case
average_case_setup = """
from __main__ import create_average_case, insertion_sort
average_case_list = create_average_case({0})"""

# list of different list lengths to run through
reps_list = [1000, 2000, 4000, 8000, 16000, 32000]

# measure time for each case & each list with length of reps_list
for i in reps_list:
    best_case_setup_formatted = best_case_setup.format(str(i))
    best_case = timeit.timeit(stmt='insertion_sort(best_case_list)', setup=best_case_setup_formatted, number=1)
    result_array_best.append(best_case)
    print("best case: ", i, " : ", best_case)

    worst_case_setup_formatted = worst_case_setup.format(str(i))
    worst_case = timeit.timeit(stmt='insertion_sort(worst_case_list)', setup=worst_case_setup_formatted, number=1)
    result_array_worst.append(worst_case)
    print("worst case: ", i, " : ", worst_case)

    average_case_setup_formatted = average_case_setup.format(str(i))
    average_case = timeit.timeit(stmt='insertion_sort(average_case_list)', setup=average_case_setup_formatted, number=1)
    result_array_average.append(average_case)
    print("average case: ", i, " : ", average_case)

plt.plot(reps_list, result_array_best)
plt.show()
plt.plot(reps_list, result_array_worst)
plt.show()
plt.plot(reps_list, result_array_average)
plt.show()
