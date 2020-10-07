import matplotlib.pyplot as plt
import timeit
import random


def merge_sort(list_):
    if len(list_) > 1:
        middle = len(list_) // 2
        left = []
        right = []
        left.extend(merge_sort(list_[:middle]))
        right.extend(merge_sort(list_[middle:]))
        # print("left: ", left)
        # print("right: ", right)
        return reduce(left, right)
    else:
        return list_

    # call merge_sort again on each part


def reduce(left, right):
    pointer_left = 0
    pointer_right = 0
    new_list = []
    while pointer_left < len(left) and pointer_right < len(right):
        if left[pointer_left] < right[pointer_right]:
            new_list.append(left[pointer_left])
            pointer_left += 1
        else:
            new_list.append(right[pointer_right])
            pointer_right += 1
    if pointer_left >= len(left):
        new_list.extend(right[pointer_right:])
    else:
        new_list.extend(left[pointer_left:])
    # print("new_list: ", new_list)
    return new_list

    # add pointer to each set
    # compare currently pointed elements and add smaller one to result set
    # add last elements (when end of one list is reached) of the other list to the result list and return result list


def create_best_case(number):
    list_ = list(range(0, number))
    return list_


def create_best_2_case(number):
    list_ = list(range(0, number))
    list_.reverse()
    return list_


def create_average_case(number):
    list_ = list(range(0, number))
    random.shuffle(list_)
    return list_


result_array_best = list()
result_array_best_2 = list()
result_array_average = list()
result_array_average_2 = list()

# setup code to run timeit.timeit with best case
best_case_setup = """
from __main__ import create_best_case, merge_sort
best_case_list = create_best_case({0})"""

# setup code to run timeit.timeit with best_2 case
best_2_case_setup = """
from __main__ import create_best_2_case, merge_sort
best_2_case_list = create_best_2_case({0})"""

# setup code to run timeit.timeit with average case
average_case_setup = """
from __main__ import create_average_case, merge_sort
average_case_list = create_average_case({0})"""


# list of different list lengths to run through
reps_list = [1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000, 256000]

# measure time for each case & each list with length of reps_list
for i in reps_list:
    best_case_setup_formatted = best_case_setup.format(str(i))
    best_case = timeit.timeit(stmt='merge_sort(best_case_list)', setup=best_case_setup_formatted, number=1)
    result_array_best.append(best_case)
    print("best case: ", i, " : ", best_case)

    best_2_case_setup_formatted = best_2_case_setup.format(str(i))
    best_2_case = timeit.timeit(stmt='merge_sort(best_2_case_list)', setup=best_2_case_setup_formatted, number=1)
    result_array_best_2.append(best_2_case)
    print("best_2 case: ", i, " : ", best_2_case)

    average_case_setup_formatted = average_case_setup.format(str(i))
    average_case = timeit.timeit(stmt='merge_sort(average_case_list)', setup=average_case_setup_formatted, number=1)
    result_array_average.append(average_case)
    print("average case: ", i, " : ", average_case)

    average_2_case_setup_formatted = average_case_setup.format(str(i))
    average_2_case = timeit.timeit(stmt='merge_sort(average_case_list)', setup=average_2_case_setup_formatted, number=1)
    result_array_average_2.append(average_2_case)
    print("average case: ", i, " : ", average_2_case)

plt.plot(reps_list, result_array_best)
plt.show()
plt.plot(reps_list, result_array_best_2)
plt.show()
plt.plot(reps_list, result_array_average)
plt.show()
plt.plot(reps_list, result_array_average_2)
plt.show()
