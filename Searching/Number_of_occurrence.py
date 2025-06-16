arr = [1, 1, 2, 2, 2, 2, 3]
target = 2


def lowerBound(arr, target):
    res = len(arr)
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] >= target:
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res


def upperBound(arr, target):
    res = len(arr)
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] > target:
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res


print(lowerBound(arr, target))
print(upperBound(arr, target))
