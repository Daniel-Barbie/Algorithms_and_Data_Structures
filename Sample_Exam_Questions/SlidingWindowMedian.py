def sliding_window_median(list_, k):
    result_list = []
    median = Median(k)
    for i in range(len(list_) - (k-1)):
        result_list.append(median.calc_median(list_[i:i+k]))
    return result_list


class Median:

    def __init__(self, k):
        self.k = k
        #self.odd = (True if k % 2 == 1 else 0)
        self.median_func = (Median._median_odd if k % 2 == 1 else Median._median_even)

    def calc_median(self, list_):
        return self.median_func(list_)

    def _median_odd(list_):
        return list_[len(list_) // 2]

    def _median_even(list_):
        middle = len(list_) // 2
        return (list_[middle - 1] + list_[middle]) / 2


l1 = [1, 3, 5]
l2 = [1, 3, 4, 5, 6, 7, 8, 9]
l3 = [1, 3, -1, -3, 5, 3, 6, 7]

print(sliding_window_median(l1, 2))
print(sliding_window_median(l2, 2))
print(sliding_window_median(l2, 3))
print(sliding_window_median(l3, 4))