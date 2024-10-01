class Solution:

	def maxProfit(self, prices: list[int]):
		if len(prices) == 0:
			return 0

		buy = [0] * len(prices)
		sell = buy.copy()
		stop = buy.copy()

		buy[0], sell[0], stop[0] = -prices[0], 0, 0
		for i in range(1, len(prices)):
			buy[i] = max(stop[i - 1] - prices[i], buy[i - 1])
			sell[i] = buy[i - 1] + prices[i]
			stop[i] = max(stop[i - 1], sell[i - 1])

		last = len(prices) - 1

		# 最后一步一定不是买
		return max(sell[last], stop[last])


if __name__ == '__main__':
	assert Solution().maxProfit([1, 2, 3, 0, 2]) == 3
	assert Solution().maxProfit([1]) == 0

