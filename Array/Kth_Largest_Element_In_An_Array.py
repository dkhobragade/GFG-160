arr = [1, 23, 12, 9, 30, 2, 50]
k = 3

# arr.sort(reverse=True)

# print(arr[k - 1])

low = 0
high = len(arr) - 1


def Partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def QuickSelect(arr, low, high, k):
    if low <= high:
        pivot = Partition(arr, low, high)

        if pivot == k:
            return arr[pivot]
        elif pivot > k:
            return QuickSelect(arr, low, pivot - 1, k)
        else:
            return QuickSelect(arr, pivot + 1, high, k)


print(QuickSelect(arr, low, high, len(arr) - k))
