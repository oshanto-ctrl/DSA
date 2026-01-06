# Binary search - iterative approach
def binary_search(arr, item):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] < item:
            low = mid + 1
        elif arr[mid] > item:
            high = mid - 1
        else:
            return mid
    return -1


arr = [2, 3, 10, 19, 40, 121, 259]
item = 2
result = binary_search(arr, item)
if result != -1:
    print("Item present at index: ", result)
else:
    print("Item not present in array!")