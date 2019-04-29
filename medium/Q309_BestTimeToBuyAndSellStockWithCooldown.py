class Solution:

	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
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
		return max(sell[last], stop[last])

	def maxProfit_old(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
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
		return max(sell[last], stop[last]) # 最后一步一定不是买


if __name__ == '__main__':
	print(Solution().maxProfit([1, 2, 3, 0, 2]))
	print(Solution().maxProfit_old([1, 2, 3, 0, 2]))
