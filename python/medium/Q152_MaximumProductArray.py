class Solution:
	"""
	乘积最大子序列
	https://leetcode-cn.com/explore/interview/card/top-interview-questions-hard/60/dynamic-programming/154/
	"""

	def maxProduct(self, nums):
		"""
		该解法的关键是认识到存在负数时，最小值可能由负负得正变为最大值。
		所以不仅要记录最大，还要记录最小
		"""
		if len(nums) == 0:
			return None

		# 子序列最大值， 子序列最小值， 全局最大值（结果）
		maxp, minp, r = nums[0], nums[0], nums[0]

		for i in range(1, len(nums)):
			p = nums[i]
			tmax, tmin = maxp * p, minp * p

			maxp = max(tmax, tmin, p)
			minp = min(tmax, tmin, p)
			r = max(maxp, r)
		return r

	def force(self, nums):
		"""
		暴力搜索，时间O(n^2)，可能会超时
		"""
		maxp = nums[0]
		for i in range(len(nums)):
			p = nums[i]
			maxp = max(maxp, p)
			for j in range(i - 1, -1, -1):
				p *= nums[j]
				maxp = max(maxp, p)
		return maxp


if __name__ == '__main__':
	print(Solution().maxProduct([2, 3, -2, 4]))
	print(Solution().maxProduct([-2, 0, -1]))
	print(Solution().maxProduct([0, 2]))  # 2
