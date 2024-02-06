# an array of integers
my_array = [2, 7, 3, 9, 12, 11,5]

# Calculate the length of array
n = len(my_array)

# Loop through array, starting from second element
for i in range(n-1):
 # Assume no swapping has occurred in this pass
    swapped = False

    # Loop through the array, starting from the current element
    for j in range(n-i-1):
        # If the current element is greater than the next element
        if my_array[j] > my_array[j+1]:
            # Swap the current and next elements
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
            # Set the swapped flag to True
            swapped = True
    
    # If no swapping occurred in this pass, the array is already sorted
    if not swapped:
        break

# Print the sorted array
print("Sorted array:", my_array)