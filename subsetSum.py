def subsetSum(arr, n, i, target_sum, count):
    # Base case: If we have reached the end of the array
    if i == n:
        # Check if the remaining sum is 0, then increment the count
        if target_sum == 0:
            return count + 1
        else:
            return count
    
    # Recursive case:
    # Include the current element in the subset and move to the next index
    count = subsetSum(arr, n, i + 1, target_sum - arr[i], count)
    
    # Exclude the current element from the subset and move to the next index
    count = subsetSum(arr, n, i + 1, target_sum, count)
    
    return count

# Input array
arr = []
size = int(input("Enter the size of the array: "))
for j in range(size):
    value = int(input(f"Enter element {j + 1}: "))
    arr.append(value)

# Target sum
target_sum = int(input("Enter the target sum: "))
n = len(arr)

# Call the subsetSum function and print the result
result = subsetSum(arr, n, 0, target_sum, 0)
print(f'The total number of subsets with the sum {target_sum} is: {result}')
