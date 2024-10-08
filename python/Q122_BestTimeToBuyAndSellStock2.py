class Solution:

	def maxProfit(self, prices: list[int]) -> int:
		"""
		在一天之内能卖了再买的情况下，利润就是前面大的减小的。
		即使卖出后出现更大的，也可以立即买回，所以直接加就完事。
		"""
		result = 0
		for i in range(1, len(prices)):
			profit = prices[i] - prices[i - 1]
			if profit > 0:
				result += profit
		return result

	def maxProfit_dp(self, prices: list[int]) -> int:
		"""
		每天只能操作一次的情况下是一个动态规划问题
		"""
		if len(prices) < 2:
			return 0
		buy, sell = [0] * len(prices), [0] * len(prices)
		buy[0], sell[0] = -prices[0], 0

		for i in range(1, len(prices)):
			buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])
			sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

		return max(buy[len(prices) - 1], sell[len(prices) - 1])


if __name__ == '__main__':
	print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
	print(Solution().maxProfit([1, 2, 3, 4, 5]))
	print(Solution().maxProfit([7, 6, 4, 3, 1]))
