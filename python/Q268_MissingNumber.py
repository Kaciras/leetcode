class Solution:

	def missingNumber(self, nums: list[int]) -> int:
		"""只缺失一个数的话可以直接减出来"""
		return len(nums) * (len(nums) + 1) // 2 - sum(nums)


if __name__ == '__main__':
	print(Solution().missingNumber([3,0,1]))
	print(Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
