def print_fibonacci(number):
    result_list = []
    i = 1
    n = 1
    result_list.append(n)
    print(n)
    while n < number:
        result_list.append(n)
        print(n)
        i_old = i
        i = n
        n = i_old+n
    return result_list

print_fibonacci(10000)