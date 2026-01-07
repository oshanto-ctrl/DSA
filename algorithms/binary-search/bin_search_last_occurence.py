'''
Variant 3: Last occurrence of key (index of array) 

Input : 2 3 3 5 5 5 6 6
Function : last(3)
Returns : 2

Function : last(5)
Returns : 5

Function : last(4)
Returns : -1
'''
def last_occurence(arr, target):
    left, right = 0, len(arr) - 1
    found_at = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            found_at = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return found_at

arr = [2, 3, 3, 5, 5, 5, 6, 6]
# target = 3
# target = 5
target = 2
# target = -1
result_index = last_occurence(arr, target)
if result_index >= 0:
    print(f"Target = {target} Found at index {result_index}")
else:
    print(f"Wasn't found any last occurence. Returned with {result_index}")


