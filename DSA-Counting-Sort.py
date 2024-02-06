# This function sorts an array using the counting sort algorithm
def countingSort(arr):

    # Find the maximum value in the array
    max_val = max(arr)
    # Initialize a count array with size equal to max_val + 1
    # Each index in the count array represents a number in the range of max_val
    # The value at each index represents the number of occurrences of that number in the input array
    count = [0] * (max_val + 1)

    # Iterate through the input array and increment the count of each number
    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    # Iterate through the count array and add the numbers to the sorted array
    # The number of times each number is added to the sorted array is equal to its count
    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    # Return the sorted array
    return arr

# Initialize an unsorted array
unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]

# Call the counting sort function on the unsorted array
sortedArr = countingSort(unsortedArr) 




# Print the sorted array
print("Sorted arrays: ", sortedArr)


# Sorted arrays:  [1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 6] 



