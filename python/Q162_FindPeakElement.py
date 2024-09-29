VMIN = -2 ** 31 - 1  # 表示边界外的负无穷值


class Solution:

	def findPeakElement(self, nums):
		"""二分，三个一组判断形状，但好像搞复杂了"""
		lo, hi, e = 0, len(nums), len(nums) - 1

		while lo < hi:
			mid = (lo + hi) // 2
			b = nums[mid]
			a = VMIN if mid == 0 else nums[mid - 1]
			c = VMIN if mid == e else nums[mid + 1]

			if a < b > c:
				return mid
			elif a > b > c:
				hi = mid
			else:
				lo = mid + 1

	def findPeakElement_1(self, nums):
		"""最简单的想法，但题目要求对数时间"""
		nums.append(float("-inf"))

		# 总有 nums[i-1] < nums[i] 成立
		for i in range(len(nums) - 1):
			if nums[i] > nums[i + 1]:
				return i


if __name__ == '__main__':
	assert Solution().findPeakElement([1, 2, 3, 1]) == 2
	assert Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5

	assert Solution().findPeakElement([1]) == 0
	assert Solution().findPeakElement([1, 2]) == 1
	assert Solution().findPeakElement([2, 1]) == 0

	assert Solution().findPeakElement([-2147483648]) == 0
	assert Solution().findPeakElement([1, 2, 3, 4, 3]) == 3
