# This function sorts an array using the merge sort algorithm
def mergeSort(arr):
    # If the array has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle index of the array
    mid = len(arr) // 2

    # Split the array into two halves
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    # Recursively sort both halves
    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    # Merge the sorted halves and return the result
    return merge(sortedLeft, sortedRight)


# This function merges two sorted arrays into a single sorted array
def merge(left, right):
    # Create an empty array to store the merged result
    result = []

    # Initialize two pointers for the left and right arrays
    i = j = 0

    # While there are still elements in both arrays
    while i < len(left) and j < len(right):
        # If the current element in the left array is smaller
        if left[i] < right[j]:
            # Add it to the result and move to the next element in the left array
            result.append(left[i])
            i += 1
        else:
            # Otherwise, add the current element in the right array to the result
            # and move to the next element in the right array
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left and right arrays to the result
    result.extend(left[i:])
    result.extend(right[j:])

    # Return the merged and sorted result
    return result


# Define an unsorted array
unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]

# Sort the array using the merge sort function
sortedArr = mergeSort(unsortedArr)

# Print the sorted array
print("Sorted array:", sortedArr)

# Sorted array: [-13, -10, 3, 6, 7, 15, 23.5, 55]
