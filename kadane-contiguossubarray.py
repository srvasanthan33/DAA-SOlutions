# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# A subarray is a contiguous part of an array.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# For example:

# Test	Input	Result
# s.maxSubArray(A)
# 9
# -2
# 1
# -3
# 4
# -1
# 2
# 1
# -5
# 4
# The sum of contiguous sublist with the largest sum is 6


class Solution:
    def maxSubArray(self,A):
        ############ Add your Code here
        res = 0
        mm = - 10000
        for v in A:
            res += v
            mm = max(mm,res)
            if res<0:
                res = 0
        return mm

        
A =[]                  
n=int(input())
for i in range(n):
    A.append(int(input()))
s=Solution()
print("The sum of contiguous sublist with the largest sum is",s.maxSubArray(A))
 