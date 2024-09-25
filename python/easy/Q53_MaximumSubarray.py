class Solution:

	def maxSubArray(self, nums: list[int]):
		"""c 是当前子序列的和，m 是最大子序列的和"""
		c, m = 0, nums[0]
		for n in nums:
			c += n
			if c < n: c = n
			if c > m: m = c
		return m


if __name__ == '__main__':
	print(Solution().maxSubArray([-2, -1]))
	print(Solution().maxSubArray([-1]))
	print(Solution().maxSubArray([-3, -2, 0, -1]))
	print(Solution().maxSubArray([1]))
	print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
