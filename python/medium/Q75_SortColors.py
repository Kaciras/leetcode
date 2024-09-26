import collections


class Solution:

	def sortColors(self, nums: list[int]):
		"""计数排序，专用于这种类型有限的情况"""
		colors = collections.Counter(nums)
		s1 = colors[0] + colors[1]

		for i in range(colors[0]):
			nums[i] = 0
		for i in range(colors[0], s1):
			nums[i] = 1
		for i in range(s1, s1 + colors[2]):
			nums[i] = 2

	def sortColors_1(self, nums: list[int]):
		"""俩指针 a, b 分别是红白的末尾，将数组分成三份"""
		a = b = 0
		for i in range(len(nums)):
			if nums[i] == 0:
				nums[a], nums[i] = nums[i], nums[a]
				a += 1
				if b < a:  # 处理一开始全在一起的情况
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
