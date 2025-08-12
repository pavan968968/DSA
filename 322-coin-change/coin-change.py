class Solution:
    def coinChange(self, coins, amount):
        # Initialize dp array
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0  # Base case
        
        # Fill dp array
        for curr_amount in range(1, amount + 1):
            for coin in coins:
                if coin <= curr_amount:
                    dp[curr_amount] = min(dp[curr_amount], dp[curr_amount - coin] + 1)
        
        return dp[amount] if dp[amount] != amount + 1 else -1

