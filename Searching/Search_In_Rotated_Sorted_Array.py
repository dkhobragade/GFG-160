arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 3


low = 0
high = len(arr) - 1

while low <= high:
    mid = low + (high - low) // 2

    if arr[mid] == key:
        print(mid)
        break

    if arr[mid] >= arr[low]:

        if key >= arr[low] and key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    else:

        if key > arr[mid] and key <= arr[high]:
            low = mid + 1
        else:
            high = mid - 1
