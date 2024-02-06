def binary_search(arr, value):
    left = 0
    right = len(arr) - 1
    mid = (left + right) // 2

    while arr[mid] != value:
        if value > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
        if left >= right:
            break
    if value == arr[mid]:
        return mid
    else:
        return "No such value"


check = [1, 1, 6, 15, 15, 19, 25, 31, 35]
print(binary_search(check, 19))