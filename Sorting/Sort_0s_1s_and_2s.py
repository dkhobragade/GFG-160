arr = [0, 1, 2, 0, 1, 2]

# n = len(arr)
# low = 0
# mid = 0
# high = n - 1


# while mid <= high:
#     if arr[mid] == 0:
#         arr[mid], arr[low] = arr[low], arr[mid]
#         mid += 1
#         low += 1
#     elif arr[mid] == 1:
#         mid += 1
#     else:
#         arr[mid], arr[high] = arr[high], arr[mid]
#         high -= 1
# print(arr)


n = len(arr)
low = 0
mid = 0
high = n - 1

while mid <= high:
    if arr[mid] == 0:
        arr[low], arr[mid] = arr[mid], arr[low]
        mid += 1
        low += 1
    elif arr[mid] == 1:
        mid += 1
    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -= 1
print(arr)
