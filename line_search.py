def line_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

arr = [12, 14, 1, 22, 100, 15, 24, 78]
target = 14

print(line_search(arr, target))


