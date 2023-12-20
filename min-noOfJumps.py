# Create a python program to find Minimum number of jumps to reach end  of the array using naive method(recursion)

def minJumps(arr, l, h):
    if h == l:
        return 0
    if arr[l] == 0:
        return float('inf')
    min_jumps = float('inf')

    for i in range(l + 1, h + 1):
        if i <= l + arr[l]:
            jumps = minJumps(arr, i, h)
            if jumps != float('inf') and jumps + 1 < min_jumps:
                min_jumps = jumps + 1

    return min_jumps

# Input array
arr = []
n = int(input("Enter the size of the array: "))
for i in range(n):
    arr.append(int(input("Enter element {}: ".format(i))))

# Calculate and print the minimum number of jumps
print('Minimum number of jumps to reach end is', minJumps(arr, 0, n - 1))

 