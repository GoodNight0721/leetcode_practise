class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [1, 0, 1]

        for i in range(1, len(obstacles)):
            if obstacles[i] != 0:
                blocked = obstacles[i] - 1
                dp[blocked] = float('inf')
            
            best = min(dp)

            for j in range(3):
                if obstacles[i] != j + 1:
                    dp[j] = min(dp[j], best + 1)

        return min(dp)