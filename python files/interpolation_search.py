
# The Interpolation Search is an improvement over Binary Search for instances,
# where the values in a sorted array are uniformly distributed. Binary Search 
# always goes to the middle element to check. On the other hand, interpolation 
# search may go to different locations according to the value of the key being 
# searched. For example, if the value of the key is closer to the last element,
# interpolation search is likely to start search toward the end side.

# The idea of formula is to return higher value of pos
# when element to be searched is closer to arr[hi]. And
# smaller value when closer to arr[lo]
# pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]
# arr[] ==> Array where elements need to be searched
# x     ==> Element to be searched
# lo    ==> Starting index in arr[]
# hi    ==> Ending index in arr[]

def interpolation_search(arr, x, n):
	# Find indexs of two corners 
    lo = 0
    hi = (n - 1) 
   
    # Since array is sorted, an element present 
    # in array must be in range defined by corner 
    while lo <= hi and x >= arr[lo] and x <= arr[hi]: 
        if lo == hi: 
            if arr[lo] == x:  
                return lo; 
            return -1; 
          
        # Probing the position with keeping 
        # uniform distribution in mind. 
        pos  = lo + int(((float(hi - lo) / 
            ( arr[hi] - arr[lo])) * ( x - arr[lo]))) 
  
        # Condition of target found 
        if arr[pos] == x: 
            return pos 
   
        # If x is larger, x is in upper part 
        if arr[pos] < x: 
            lo = pos + 1; 
   
        # If x is smaller, x is in lower part 
        else: 
            hi = pos - 1; 
      
    return -1

# Driver code to test function 
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 
    34, 55, 89, 144, 233, 377, 610 ] 
x = 233
n = len(arr) 

# Find the index of 'x' using Jump Search 
index = interpolation_search(arr, x, n) 

# Print the index where 'x' is located 
print(f"Number {x} is at index : {index}") 

#Time Complexity : O(log(log n))
