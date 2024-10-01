class Solution:

	def moveZeroes(self, nums: list[int]):
		j = 0
		for i in range(len(nums)):
			if nums[i] != 0:
				nums[j] = nums[i]
				j += 1
		while j < len(nums):
			nums[j] = 0
			j += 1


def test(nums):
	Solution().moveZeroes(nums)
	print(nums)


if __name__ == '__main__':
	test([])
	test([0, 1, 0, 3, 12])
	test([0, 0])
