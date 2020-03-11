# Python program for implementation of Selection 
def selectionSort(arr):
    # Traverse through all array elements 
    for i in range(len(arr)):

        # Find the minimum element in remaining  
        # unsorted array 
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j

        # Swap the found minimum element with  
        # the first element 
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
  
# Driver code to test above 
A = [64, 25, 8]
result = selectionSort(A)
print ("Sorted array: ") 
for i in range(len(result)): 
    print(f"Value at {i} is: {result[i]}")

