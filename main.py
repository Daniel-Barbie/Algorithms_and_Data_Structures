from insertion_sort import insertion_sort

if __name__ == '__main__':
    # random sorting
    elements = [5, 1, 4, 3, 2, 7, 9, 8, 6]
    # fully sorted
    elements1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # fully sorted, opposite way ("perfectly unsorted")
    elements2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    # random sorting, negative values included
    elements3 = [1, 2.4, 5345.3, 45.3, 45, 6, 3, 23, 41, 234, 52, 345, 2345, 6, 3, 4, -1, -5, -23, -9.2, 34, 5]
    print(f'First run: random positions: {insertion_sort(elements)}')
    print(f'Second run: perfectly sorted: {insertion_sort(elements1)}')
    print(f'Third run: perfectly unsorted: {insertion_sort(elements2)}')
    print(f'Fourth run: random sorting, negative values included: {insertion_sort(elements3)}')