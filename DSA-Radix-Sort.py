# Initialize an array called 'myArray' with some integer values
myArray = [170, 45, 75, 90, 802, 24, 2, 66]

# Initialize buckets for each digit0-9) store the elements of 'myArray'
#during the sorting process
radixArray = [[] for _ in range(10)]

# Find the maximum value in 'myArray' and store it in 'maxVal'
maxVal = max(myArray)

# Initialize 'exp' to 1
exp = 1

# Continue the following process while 'maxVal' divided by 'exp' is greater than 0
while maxVal // exp > 0:
   
   # Distribute elements of 'myArray' into the 'radixArray' buckets based on their digit at 'exp' position
   for val in myArray:
       radixIndex = (val // exp) % 10
       radixArray[radixIndex].append(val)

   # Collect elements from 'radixArray' buckets and update 'myArray' with the sorted elements
   myArray = [val for bucket in radixArray for val in bucket]

   # Clear 'radixArray' buckets for the next iteration
   radixArray = [[] for _ in range(10)]

   # Multiply 'exp' by 10 to move to the next digit position for the next iteration
   exp *= 10

# Print the sorted array
print("Sorted array:", myArray)


#  Sorted array: [2, 24, 45, 66, 75, 90, 170, 802] 

