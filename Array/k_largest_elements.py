arr = [12, 5, 787, 1, 23]
k = 2

low = 0
high = len(arr) - 1


# def Divide(arr, low, high):
#     if low < high:
#         mid = (low + high) // 2
#         Divide(arr, low, mid)
#         Divide(arr, mid + 1, high)
#         Merge(arr, low, high, mid)


# def Merge(arr, low, high, mid):
#     left = low
#     right = mid + 1
#     temp = []

#     while left <= mid and right <= high:
#         if arr[left] < arr[right]:
#             temp.append(arr[right])
#             right += 1
#         else:
#             temp.append(arr[left])
#             left += 1
#     while left <= mid:
#         temp.append(arr[left])
#         left += 1

#     while right <= high:
#         temp.append(arr[right])
#         right += 1

#     for i in range(len(temp)):
#         arr[low + i] = temp[i]


# Divide(arr, low, high)
# print(arr[:k])


def Parition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def Quick(arr, low, high):
    if low < high:
        pivot = Parition(arr, low, high)
        Quick(arr, low, pivot - 1)
        Quick(arr, pivot + 1, high)


Quick(arr, low, high)
print(arr[:k])
