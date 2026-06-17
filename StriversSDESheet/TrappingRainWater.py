class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        if n == 0:
            return 0

        # Prefix Max Array
        prefix = [0] * n
        prefix[0] = height[0]

        for i in range(1, n):
            prefix[i] = max(prefix[i - 1], height[i])

        # Suffix Max Array
        suffix = [0] * n
        suffix[n - 1] = height[n - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i])

        # Calculate trapped water
        total = 0

        for i in range(n):
            total += min(prefix[i], suffix[i]) - height[i]

        return total
