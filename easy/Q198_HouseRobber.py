from typing import List


class Solution:

	def rob(self, nums: List[int]) -> int:
		"""最大收益 = max(前第二个偷了的 + 这次收益，前一个的收益)"""
		if len(nums) == 0:
			return 0

		steal = last_steal = 0
		for n in nums:
			prev2, last_steal = last_steal, steal
			steal = max(prev2 + n, steal)

		return steal


if __name__ == '__main__':
	assert Solution().rob([1, 2, 3, 1]) == 4
	assert Solution().rob([2, 7, 9, 3, 1]) == 12
	assert Solution().rob([100]) == 100
	assert Solution().rob([100, 200]) == 200
