arr = [1, 2, 4, 5, 7, 8, 3]

n = len(arr)

low = 0
high = n - 1

while low < high:
    mid = low + (high - low) // 2

    if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:
        print(mid)
        break

    elif arr[mid] < arr[mid + 1]:
        low = mid + 1
    else:
        high = mid - 1
