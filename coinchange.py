# Coins with different denominations like 1¢, 5¢ and 10¢ are given.
#  Identify a solution to make an amount by using these coins such that a minimum number of coins are used. Explain the algorithm in detail 

# Create a python function to compute the fewest number of 
# coins that we need to make up the amount given for coin change problem using dynamic programming

def count(S, n, target):
    if target == 0:
        return 1
    if target < 0 or n < 0:
        return 0 
    incl = count(S, n, target - S[n])
    excl = count(S, n - 1, target)
    return incl + excl

if __name__ == '__main__':
    S = [1, 5, 10]  # Coin denominations: 1¢, 5¢, 10¢
    n = len(S)      # Number of coin denominations
    target = int(input("Enter the amount to make: "))
    
    # Call the count function to calculate the total number of ways to make the desired amount.
    result = count(S, n - 1, target)
    
    print(f'The total number of ways to make ${target/100:.2f} using the given coins is {result}.')
