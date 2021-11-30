# bestcase 1 item present  worst case always n and avg case item present n/2

def sequence_search_unordered(arr, item):
    pos = 0
    found = False
    while pos < len(arr) and not found:
        if arr[pos] == item:
            found = True
        else:
            pos += 1
    return found


# item present or not : 1 best case and worst case is n and avg case is n/2
def sequence_search_ordered(arr, item):
    pos = 0
    found = False
    stopped = False
    while pos < len(arr) and not found and not stopped:
        if arr[pos] == item:
            found = True
        else:
            if arr[pos] > item:
                stopped = True

            else:
                pos += 1

    return found


# the time analyses goes here
# the iterative version for binary search
def binary_search_iterative(arr, item):
    first = 0
    last = len(arr) - 1
    found = False
    while first <= last and not found:
        mid = (first + last) / 2
        if arr[mid] == item:
            found = True
        else:
            if item < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found


# the recursive version for binary search

def binary_search_recursive(arr, item):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) / 2
        if arr[mid] == item:
            return True
        else:
            if item < arr[mid]:
                return binary_search_recursive(arr[:mid], item)
            else:
                return binary_search_recursive(arr[mid + 1:], item)

