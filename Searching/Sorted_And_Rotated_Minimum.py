arr = [4, 2, 3]


low = 0
high = len(arr) - 1

while low < high:
    mid = low + (high - low) // 2

    if arr[mid] < arr[mid + 1] and arr[mid] < arr[mid - 1]:
        print(arr[mid])
        break
    elif arr[mid - 1] > arr[mid]:
        mid = high
    else:
        mid = low
