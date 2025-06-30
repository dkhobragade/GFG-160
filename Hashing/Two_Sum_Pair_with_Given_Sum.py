arr = [11]
target = 11


def SumPair(arr):
    for i in range(1, len(arr)):
        for j in range(len(arr) - 1):
            if arr[i] + arr[j] == target:
                return True
    return False


print(SumPair(arr))
