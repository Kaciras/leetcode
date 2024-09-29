from typing import List

from utils import benckmark


class Solution:
	"""float(inf) 改成 0x7FFFFFFF，耗时降低 0.2s/Mops"""

	def maxProfit(self, prices: List[int]) -> int:
		buy, r = 0x7FFFFFFF, 0
		for p in prices:
			buy = min(buy, p)
			r = max(p - buy, r)
		return r


if __name__ == '__main__':
	print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
	print(Solution().maxProfit([7, 6, 4, 3, 1]))

	benckmark(Solution().maxProfit, [7, 1, 5, 3, 6, 4])
