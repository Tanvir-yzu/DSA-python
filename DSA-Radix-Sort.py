def countingSort(arr, exp1):
    n = len(arr)  # Get the length of the array
    output = [0] * n  # Initialize output array of the same length
    count = [0] * 10  # Initialize count array for digits 0-9

    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # Change count[i] so it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers
    for i in range(n):
        arr[i] = output[i]


def radixSort(arr):
    # Find the maximum number to know the number of digits
    max1 = max(arr)
    exp = 1  # Start with the least significant digit
    # Continue until we've sorted by the largest digit
    while max1 // exp > 0:
        countingSort(arr, exp)  # Sort arr[] for the current digit
        exp *= 10  # Move to the next digit


# Example usage
if __name__ == "__main__":
    myArray = [170, 45, 75, 90, 802, 24, 2, 66]  # Example array
    radixSort(myArray)  # Sort the array
    print("Sorted array:", myArray)  # Print the sorted array
    
    # Sorted array: [2, 24, 45, 66, 75, 90, 170, 802]
