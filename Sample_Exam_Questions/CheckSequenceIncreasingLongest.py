def check_sequence(list_):
    i = 1
    n = 0
    n_start = 0
    n_max = 0
    n_max_start = 0
    n_max_end = 0
    while i < len(list_):
        if list_[i - 1] < list_[i]:
            n += 1
        else:
            if n > n_max:
                n_max = n
                n = 0
                n_max_start = n_start
                n_max_end = i
            n_start = i
        i += 1
    if n > n_max or n_max_end == 0:
        n_max_start = n_start
        n_max_end = i
    return list_[n_max_start:n_max_end]


print(check_sequence([1, 2, 3, 4, 5, 10, 7, 8, 9, 10, 11, 12, 13, 14]))
