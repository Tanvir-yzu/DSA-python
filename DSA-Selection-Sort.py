# Initialize an array of integers
my_array = [2, 7, 3, 9, 12, 11, 5]

# Calculate the length of array
n = len(my_array)

# Loop through each element in the array
for i in range(n):
    # Assume the current element is the smallest one found so far
    min_i = i

    # Loop through the remaining elements in the array
    for j in range(i + 1, n):
        # If a smaller element is found
        if my_array[j] < my_array[min_i]:
            # Update the index of the smallest element found so far
            min_i = j

    # Swap the current element with the smallest element found so far
    my_array[i], my_array[min_i] = my_array[min_i], my_array[i]

# Print the sorted array
print('sorted array', my_array)

# sorted array [2, 3, 5, 7, 9, 11, 12]
