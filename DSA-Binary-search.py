# This function performs a binary search on a sorted array to find a target value
def binarySearch(arr, targetVal):

    # Initialize the left and right indices of the search range
    left = 0
    right = len(arr) - 1

    # Continue the search while the left index is less than or equal to the right index
    while left <= right:

        # Calculate the middle index of the current search range
        mid = (left + right) // 2

        # If the middle element is equal to the target value, return the middle index
        if arr[mid] == targetVal:
            return mid

        # If the middle element is less than the target value, narrow the search range to the right half
        if arr[mid] < targetVal:
            left = mid + 1

        # If the middle element is greater than the target value, narrow the search range to the left half
        else:
            right = mid - 1

    # If the target value is not found in the array, return -1
    return -1


# Define a sorted array of integers
myArray = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# Define the target value to be searched
myTarget = 15

# Call the binarySearch function with the array and target value as arguments
result = binarySearch(myArray, myTarget)

# Print the result of the binary search
if result != -1:
    print("Value", myTarget, "found at index", result)
else:
    print("Target not found in array.")
    
    # Value 15 found at index 7
    
    
