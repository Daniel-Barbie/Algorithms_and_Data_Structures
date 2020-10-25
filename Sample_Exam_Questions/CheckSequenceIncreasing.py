def check_sequence_increasing(list_):
    i = 1
    while i < len(list_):
        if list_[i-1] < list_[i]:
            i += 1
        else:
            return False
    return True


print(check_sequence_increasing([1,2,3,4,5,6,7,9,8]))