mat = [[3, 4, 9], [2, 5, 6], [9, 25, 27]]
x = 9


def search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if x == arr[mid]:
            return True

        elif x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


n = len(mat)
m = len(mat[0])

for i in range(n):
    if search(mat[i], x):
        print(True)
        break
print(False)
