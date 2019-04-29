class Solution:

	def canJump(self, nums):
		if len(nums) < 2:
			return True
		first = len(nums) - 1 # 能够跳到终点的最前位置

		for i in range(len(nums) - 1, -1, -1):
			if i + nums[i] >= first:
				first = i
		return first == 0

	def canJump_my(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if len(nums) < 2:
			return True

		maximum, i = nums[0], 1
		while i <= maximum:
			c = i + nums[i]
			if c >= len(nums) - 1:
				return True
			maximum = max(maximum, c)
			i += 1
		return False


if __name__ == '__main__':
	print(Solution().canJump([0]))
	print(Solution().canJump([]))
	print(Solution().canJump([1, 2]))
	print(Solution().canJump([2, 3, 1, 1, 4]))
	print(Solution().canJump([3, 2, 1, 0, 4]))
	print(Solution().canJump([99, 0, 0, 0, 0]))
