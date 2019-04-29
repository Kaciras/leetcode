class Solution:

	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		buy, r = float("inf"), 0
		for p in prices:
			buy = min(buy, p)
			r = max(p - buy, r)
		return r


if __name__ == '__main__':
	print(Solution().maxProfit([7,1,5,3,6,4]))
	print(Solution().maxProfit([7,6,4,3,1]))
