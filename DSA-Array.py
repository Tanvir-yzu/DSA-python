# Initialize an array with five integer values
my_array = [7, 12, 9, 4, 11]

# Set the initial minimum value to the first element of the array
minVal = my_array[0]

# Iterate through each element in the array
for i in my_array:
    # If the current element is less than the minimum value, update the minimum value
    if i < minVal:
        minVal = i
        # Print the new minimum value
        print('Lowest value : ', minVal)