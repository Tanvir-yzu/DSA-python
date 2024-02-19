def countingSort(arr):
    # Initialize a count array with zeros, size based on the maximum value in `arr`
    count = [0] * (max(arr) + 1)

    # Increment the count for each number in `arr`
    for num in arr:
        count[num] += 1

    # Reconstruct `arr` using the counts stored in `count`
    index = 0  # Start from the first position of `arr`
    for i, cnt in enumerate(count):  # `i` is the number, `cnt` is its count
        for _ in range(cnt):  # Repeat `cnt` times for each number `i`
            arr[index] = i  # Place `i` in `arr`
            index += 1  # Move to the next position in `arr`
    return arr  # Return the sorted array

# Example usage
unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]  # An unsorted array
sortedArr = countingSort(unsortedArr)  # Sort the array using counting sort
print("Sorted array: ", sortedArr)  # Print the sorted array
#Sorted array:  [1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6]

