# an O(T * m²) solution

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = points
        for i in range(1, len(points)):
            for j in range(len(points[i])):
                best = float('-inf')
                for k in range(len(points[i-1])):
                    best = max(best, dp[i-1][k] - abs(k - j))
                dp[i][j] += best

        return max(dp[len(points) - 1])   

# an O(T * m) solution

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = points
        for i in range(1, len(points)):
            prev = dp[i - 1]

            for j in range(1, len(points[i])):
                prev[j] = max(prev[j], prev[j-1] - 1)
            
            for j in range(len(points[i]) - 2, -1, -1):
                prev[j] = max(prev[j], prev[j+1] - 1)
            
            for j in range(len(points[i])):
                dp[i][j] += prev[j]
                
        return max(dp[len(points) - 1])                    