# First occurence of key (index of array)
# Input : 2 3 3 5 5 5 6 6
# Function : first_occurenence(3)
# Returns : 1
# Function : first_occurenence(5)
# Returns : 3
# Function : first_occurenence(4)
# Returns : -1

# Imports
import bisect

# Bisect_left() approach
def first_occurenence_bisect(arr, target):
    index = bisect.bisect_left(arr, target)
    if index < len(arr) and arr[index] == target:
        return index
    return -1

# Naive binary-search approach
def first_occurenence_naive(arr, target):
    left, right = 0, len(arr) - 1
    index = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            index = mid # Target found at mid, but continue searching left subarray
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1 # basic binary-search approach
        else:
            right = mid - 1 # basic binary-search approach
    return index

# Driver

arr = [2, 3, 3, 5, 5, 5, 6, 6]
# target = 3
# target = 5
target = 6
# target = 7 # Non-existing
# target = 0 # Less than, non-existing

print("BISECT APPROACH\n", 15*"-")
result_index_bisect = first_occurenence_bisect(arr, target)
if result_index_bisect > 0:
    print(f"Found target = {target} at arr index: {result_index_bisect} using bisect_left()")
else:
    print(f"Target = {target} wasn't found using bisect_left()! Returned with {result_index_bisect}")
print(15*"-")

print("Naive Approach ", 15*"-")
result_index_naive = first_occurenence_naive(arr, target)
if result_index_naive > 0:
    print(f"Found target = {target} at arr index: {result_index_naive} using naive appraoch")
else:
    print(f"Target = {target} wasn't found using naive approach! Returned with {result_index_naive}")
print(15*"-")
