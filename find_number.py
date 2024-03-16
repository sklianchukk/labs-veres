def find_number(lst, k):
    copy_lst = lst[:]
    if k > len(lst) or len(lst) <= 1:
        return "The length of list must be greater than 1 and greater or equal to k-position"
    else:
        start = 0
        end = len(lst) - 1
        quicksort(lst, start, end)
        num = lst[-k]
        idx = copy_lst.index(num)

    return f"Sorted array: {lst}; \nYour number: {num}; \nNumber`s position in unsorted array: {idx}."


def partition(lst, start, end):
    pivot = lst[end]
    i = start - 1
    for j in range(start, end):
        if lst[j] < pivot:
            i = i + 1
            (lst[i], lst[j]) = (lst[j], lst[i])
    (lst[i + 1], lst[end]) = (lst[end], lst[i + 1])
    return i + 1


def quicksort(lst, start, end):
    if start < end:
        pivot = partition(lst, start, end)
        quicksort(lst, start, pivot - 1)
        quicksort(lst, pivot + 1, end)
