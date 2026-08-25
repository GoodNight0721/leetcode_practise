"""
Strategy Selection with Switching Cost

You are given a 2D list pnl, where:

    pnl[t][j]

represents the profit earned on day t if you use strategy j.

You must choose exactly one strategy on each day.

If the strategy chosen today is different from the strategy chosen
on the previous day, you must pay a fixed switching cost `fee`.

Return:
1. The maximum total profit.
2. A corresponding strategy path that achieves this maximum profit.

The strategy path should contain the strategy index chosen on each day.

Target complexity:
    O(T * m)

where:
    T = number of days
    m = number of strategies
"""


def bestStrategy(pnl: list[list[int]], fee: int):
    # Write your solution here
    T = len(pnl)
    m = len(pnl[0])
    dp = pnl[0]
    parent = [[-1] * m for _ in range(T)]
    for t in range(1, T):
        best_idx = 0
        for k in range(1, m):
            if dp[k] >= dp[best_idx]:
                best_idx = k

        curr = [0] * m

        for j in range(m):
            curr[j] = pnl[t][j] + max(dp[j], dp[best_idx] - fee)
            parent[t][j] = j if dp[j] >= dp[best_idx] - fee else best_idx
        
        dp = curr
    
    end = 0
    for k in range(1, m):
        if dp[k] >= dp[end]:
            end = k
    
    max_profit = dp[end]

    path = [0] * T
    path[-1] = end
    for t in range(T - 2, -1, -1):
        path[t] = parent[t+1][path[t+1]]

    return max_profit, path


pnl = [
    [5, 1, 3],
    [2, 8, 1],
    [7, 2, 6],
    [1, 9, 2]
]

fee = 2

profit, path = bestStrategy(pnl, fee)

print("Maximum profit:", profit)
print("Strategy path:", path)