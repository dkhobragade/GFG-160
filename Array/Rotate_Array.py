arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
d = 3

d %= len(arr)


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


reverse(arr, 0, d - 1)
reverse(arr, d, len(arr) - 1)
reverse(arr, 0, len(arr) - 1)

print(arr)
