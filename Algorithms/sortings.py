# has o(n^2) time complexity

def bubble_sort(arr):
    # moving throgh the whole list
    for n in range(len(arr) - 1, 0, -1):
        # each element from start checked with its next one
        # and changed if right one has larger value
        for k in range(n):
            if arr[k] > arr[k + 1]:
                temp = arr[k]
                arr[k] = arr[k + 1]
                arr[k + 1] = temp


# has the same time complexity of o(n^2)
# and worst worst case compared to bubble sort
def selection_sort(arr):
    for n in range(len(arr) - 1, 0, -1):
        max_pos = 0
        for loc in range(1, n + 1):
            if arr[loc] > arr[max_pos]:
                max_pos = loc

        temp = arr[n]
        arr[n] = arr[max_pos]
        arr[max_pos] = temp
