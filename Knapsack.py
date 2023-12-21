# A naive recursive implementation 
# of 0-1 Knapsack Problem 

# Returns the maximum value that 
# can be put in a knapsack of 
# capacity W 



def knapSack(W, wt, val, n): 

	# Base Case 
	if n == 0 or W == 0: 
		return 0

	# If weight of the nth item is 
	# more than Knapsack of capacity W, 
	# then this item cannot be included 
	# in the optimal solution 
	if (wt[n-1] > W): 
		return knapSack(W, wt, val, n-1) 

	# return the maximum of two cases: 
	# (1) nth item included 
	# (2) not included 
	else: 
		return max( 
			val[n-1] + knapSack( 
				W-wt[n-1], wt, val, n-1), 
			knapSack(W, wt, val, n-1)) 

# end of function knapSack 


# Driver Code 
if __name__ == '__main__': 
	profit = [60, 100, 120] 
	weight = [10, 20, 30] 
	W = 50
	n = len(profit) 
	print knapSack(W, weight, profit, n) 

# This code is contributed by Nikhil Kumar Singh 



# ight in it]. The task is to put the items into the bag such that the sum of profits associated with them is the maximum possible. 

# Note: The constraint here is we can either put an item completely into the bag or cannot put it at all [It is not possible to put a part of an item into the bag].

# Examples:

# Input: N = 3, W = 4, profit[] = {1, 2, 3}, weight[] = {4, 5, 1}
# Output: 3
# Explanation: There are two items which have weight less than or equal to 4. If we select the item with weight 4, the possible profit is 1. And if we select the item with weight 1, the possible profit is 3. So the maximum possible profit is 3. Note that we cannot put both the items with weight 4 and 1 together as the capacity of the bag is 4.

# Input: N = 3, W = 3, profit[] = {1, 2, 3}, weight[] = {4, 5, 6}
# Output: 0
