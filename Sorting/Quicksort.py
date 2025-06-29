arr = [7, 6, 10, 5, 9, 2, 1, 15, 7]


low = 0
high = len(arr) - 1


# def Partition(arr, low, high):
#     mid = arr[low]
#     i = low + 1
#     j = high

#     while True:
#         while i <= high and arr[i] < mid:
#             i += 1
#         while arr[j] > mid and j >= low:
#             j -= 1
#         if i < j:
#             arr[i], arr[j] = arr[j], arr[i]
#         else:
#             break
#     arr[low], arr[j] = arr[j], arr[low]

#     return j


# def QuickSort(arr, low, high):
#     if low < high:
#         pivot = Partition(arr, low, high)
#         QuickSort(arr, low, pivot - 1)
#         QuickSort(arr, pivot + 1, high)


# QuickSort(arr, low, high)
# print(arr)


# def Partition(arr, low, high):
#     i = low - 1
#     pivot = arr[high]

#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1


# def QuickSort(arr, low, high):
#     if low < high:
#         pivot = Partition(arr, low, high)
#         QuickSort(arr, low, pivot - 1)
#         QuickSort(arr, pivot + 1, high)


# QuickSort(arr, low, high)
# print(arr)


# low = 0
# high = len(arr) - 1


# def Partition(arr, low, high):
#     i = low - 1
#     pivot = arr[high]

#     for j in range(low, high):
#         if arr[j] < pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return i + 1


# def QuickSort(arr, low, high):
#     if low < high:
#         pivot = Partition(arr, low, high)
#         QuickSort(arr, low, pivot - 1)
#         QuickSort(arr, pivot + 1, high)


# QuickSort(arr, low, high)
# print(arr)


low = 0
high = len(arr) - 1


def Partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]

    return j


def QuickSort(arr, low, high):
    if low < high:
        pivot = Partition(arr, low, high)
        QuickSort(arr, low, pivot - 1)
        QuickSort(arr, pivot + 1, high)


QuickSort(arr, low, high)

print(arr)
