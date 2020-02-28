def linear_search(arr, length, x):
	for i in range(length):
		if arr[i] == x:
			return i
	return -1

#driver code
arr = [34, 232, 7, 8, 9, 78, 53, 35, 90]
length = len(arr)
to_find = 78

result = linear_search(arr, length, to_find)

if result == -1:
	print("Number is not in the given list")
else:
	print(f"Number is at position : {result}")

#Time Complexity : O(n)