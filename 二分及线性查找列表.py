def TinearSearch(lst, key):
    for i in range(lst):
        if key == lst[i]:
            return i

    return -1


def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1

    while high >= low:
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return mid
        else:
            low = mid + 1

    return -low - 1
