class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)

        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]

        def f(ind, target):

            if ind == 0:
                if target % coins[0] == 0:
                    return target // coins[0]
                return int(1e9)

            if dp[ind][target] != -1:
                return dp[ind][target]

            notTake = f(ind - 1, target)

            take = int(1e9)
            if coins[ind] <= target:
                take = 1 + f(ind, target - coins[ind])

            dp[ind][target] = min(take, notTake)
            return dp[ind][target]

        ans = f(n - 1, amount)

        if ans >= int(1e9):
            return -1

        return ans
