arr = [1, 4, 45, 6, 10, 8]
target = 16


# def SumPair(arr):
#     for i in range(1, len(arr)):
#         for j in range(len(arr) - 1):
#             if arr[i] + arr[j] == target:
#                 return True
#     return False


# print(SumPair(arr))


def BinarySearch(arr, low, high, req):
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] == req:
            return True
        elif arr[mid] < req:
            low = mid + 1
        else:
            high = mid - 1
    return False


def SumPair(arr):
    arr.sort()

    for i in range(len(arr)):
        req = target - arr[i]

        if BinarySearch(arr, i + 1, len(arr) - 1, req):
            return True
    return False


print(SumPair(arr))
