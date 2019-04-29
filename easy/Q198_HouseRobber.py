class Solution:

	def rob(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		if len(nums) == 0:
			return 0
		if len(nums) == 1:
			return nums[0]

		steal = last_steal = 0
		for n in nums:
			temp = last_steal
			last_steal = steal
			steal = max(temp + n, steal)
		return steal


if __name__ == '__main__':
	print(Solution().rob([100]))
	print(Solution().rob([1, 2, 3, 1]))
	print(Solution().rob([2, 7, 9, 3, 1]))
