arr = [12, 11, 13, 5, 6, 7]


def Divide(arr, low, high):

    if low < high:
        mid = (low + high) // 2
        Divide(arr, low, mid)
        Divide(arr, mid + 1, high)
        Merge(arr, low, mid, high)


def Merge(arr, low, mid, high):
    left = low
    right = mid + 1
    temp = []

    while left <= mid and right <= high:
        if arr[left] > arr[right]:
            temp.append(arr[right])
            right += 1
        else:
            temp.append(arr[left])
            left += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(len(temp)):
        arr[low + i] = temp[i]


Divide(arr, 0, len(arr) - 1)
print(arr)
