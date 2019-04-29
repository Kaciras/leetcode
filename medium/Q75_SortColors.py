class Solution:
	def sortColors(self, nums):
		"""
		:type nums: List[int]
		:rtype: void Do not return anything, modify nums in-place instead.
		"""
		a = b = 0
		for i in range(len(nums)):
			if nums[i] == 0:
				nums[a], nums[i] = nums[i], nums[a]
				a += 1
				if b < a: # 处理一开始指针全在一起的情况
					b += 1
			if nums[i] == 1:
				nums[b], nums[i] = nums[i], nums[b]
				b += 1


def test(nums):
	Solution().sortColors(nums)
	print(nums)


if __name__ == '__main__':
	test([0, 1])
	test([2, 0, 2, 1, 1, 0])
	test([])
	test([2, 0])
	test([2, 1, 0])
	test([2, 2, 0, 1, 0, 2, 2, 0, 1, 1])
