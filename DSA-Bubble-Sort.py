# an array of integers to be sorted
my_array = [2, 7, 3, 9, 12, 11, 5]

# Bubble Sort algorithm
for i in range(len(my_array)):
    # Inner loop to compare array elements
    for j in range(0, len(my_array) - i - 1):
        # Compare each pair of adjacent elements
        if my_array[j] > my_array[j + 1]:
            # Swap them if they are in the wrong order
            my_array[j], my_array[j + 1] = my_array[j + 1], my_array[j]

# Print the sorted array
print("Sorted array:", my_array)

# Sorted array: [2, 3, 5, 7, 9, 11, 12]