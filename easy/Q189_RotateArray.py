class Solution:

	def rotate(self, nums, k):
		"""
		:type nums: List[int]
		:type k: int
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		if len(nums) < 2:
			return
		i = len(nums) - k % len(nums)
		nums[:i] = nums[i - 1::-1]
		nums[i:] = nums[:i - 1:-1]
		nums.reverse() # nums[:] = nums[-i:] + nums[:-i]


def test(nums, k):
	Solution().rotate(nums, k)
	print(nums)


if __name__ == '__main__':
	test([1, 2], 1)  # [2, 1]
	test([1, 2], 2) # [1, 2]
	test([1], 1) # [1]
	test([1, 2, 3, 4, 5, 6, 7], 3)  # [5,6,7,1,2,3,4]
	test([-1, -100, 3, 99], 2)  # [3,99,-1,-100]
