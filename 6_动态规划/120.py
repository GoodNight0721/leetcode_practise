class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0] * len(triangle)

        dp[0] = triangle[0][0]

        for i in range(1, len(triangle)):
            prev_dp = dp.copy()
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[j] += triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[j] = prev_dp[j-1] + triangle[i][j]
                else:
                    dp[j] = min(prev_dp[j], prev_dp[j-1]) + triangle[i][j]
        
        return min(dp)

