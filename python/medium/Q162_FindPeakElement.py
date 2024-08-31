class Solution:
	def findPeakElement(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		nums.append(float("-inf"))
		i = 0

		# 总有 nums[i-1] < nums[i] 成立
		while i < len(nums) - 1:
			if nums[i] > nums[i + 1]:
				return i
			i += 1


if __name__ == '__main__':
	print(Solution().findPeakElement([1, 2, 3, 1]))
	print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
