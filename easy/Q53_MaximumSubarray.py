class Solution:

	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		squene, maxnum = 0,  nums[0]
		for n in nums:
			squene += n
			if squene < n: squene = n
			if squene > maxnum: maxnum = squene
		return maxnum


if __name__ == '__main__':
	print(Solution().maxSubArray([-2, -1]))
	print(Solution().maxSubArray([-1]))
	print(Solution().maxSubArray([-3, -2, 0, -1]))
	print(Solution().maxSubArray([1]))
	print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
