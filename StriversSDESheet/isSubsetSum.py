class Solution:
    def isSubsetSum(self, arr, target):
        n=len(arr)
        dp=[[-1] * (target+1) for _ in range(n)]
        def solve(i,target):
            if target==0:
                return True
            if i==0:
                return arr[0]==target
            if dp[i][target]!=-1:
                return dp[i][target]
            notTake=solve(i-1,target)
            Take=False
            if arr[i]<=target:
                Take=solve(i-1,target-arr[i])
            dp[i][target]=Take or notTake
            return dp[i][target]
        return solve(n-1,target)
