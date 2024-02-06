# Initialize an array of integers
my_array = [64, 34, 25, 12, 22, 11, 90, 5] 

# Calculate the length of the array
n = len(my_array) 

# Iterate through the array, starting from the second element
for i in range(1, n):
    
    # Set the initial index and value for the current element
    insert_index = i 
    current_value = my_array[i] 

    # Iterate through the array in reverse order, starting from the element before the current one
    for j in range(i - 1, -1, -1):
        
        # If the current element is greater than the previous one
        if my_array[j] > current_value:
            
            # Shift the previous element to the right by one position
            my_array[j + 1] = my_array[j] 

            # Update the index where the current element should be inserted
            insert_index = j 
        else:
            # If the current element is less than or equal to the previous one, break the loop
            break 

    # Insert the current element at the calculated index
    my_array[insert_index] = current_value

# Print the sorted array
print("Sorted array is :", my_array)