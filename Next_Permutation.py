arr = [2, 4, 1, 7, 5, 0]

pivot = -1

for i in range(len(arr) - 1, -1, -1):
    print
    if arr[i - 1] < arr[i]:
        pivot = i - 1
        break

if pivot == -1:
    arr.reverse()

for i in range(len(arr) - 1, pivot, -1):
    if arr[i] > arr[pivot]:
        arr[i], arr[pivot] = arr[pivot], arr[i]
        break

left = pivot + 1
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print(arr)
