class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {0:cost[0], 1:cost[1]}

        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
            del dp[i-2]

        return min(dp[len(cost)-1],dp[len(cost)-2])