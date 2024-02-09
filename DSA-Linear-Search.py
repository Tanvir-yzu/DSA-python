# This function performs a linear search on an array for a target value
def linearSearch(arr, target):

    # Iterate through the array
    for i in range(len(arr)):
        # Check if the current element in the array is equal to the target value
        if arr[i] == target:
            # If found, return the index of the target value
            return i

    # If the target value is not found in the array, return -1
    return -1



# Define the array and target value to search for
arr = [3, 2, 9, 5]
targetVal = 9

# Call the linearSearch function and store the result
result = linearSearch(arr, targetVal)

# Check if the target value is found or not
if result != -1:
    print("Value",targetVal,"found at index",result)
else:
    print("Value",targetVal,"not found")
    
    
    
