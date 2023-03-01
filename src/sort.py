# Partition for quick sort, only for numpy array
def partition(arr, low, high, key):
    i = low - 1
    pivot = arr[high][key]
    for j in range(low, high):
        if (arr[j][key] <= pivot):
            i += 1
            arr[[i, j]] = arr[[j, i]]
        
    arr[[high, i + 1]] = arr[[i + 1, high]]
    return i + 1

# Quick sort algorithm
def quick_sort(arr, low, high, key):
    if low < high:
        mid = partition(arr, low, high, key)
        quick_sort(arr, mid + 1, high, key)
        quick_sort(arr, low, mid - 1, key)