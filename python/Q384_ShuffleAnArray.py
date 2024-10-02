from random import randint


class Solution:
	"""保存两个数组来避免每次都复制一份"""

	def __init__(self, nums: list[int]):
		self.nums = nums
		self.output = nums.copy()

	def reset(self):
		return self.nums

	def shuffle(self):
		"""最简单的 Fisher–Yates 算法"""
		c = self.output
		for i in range(len(c) - 1, 0, -1):
			j = randint(0, i)
			c[i], c[j] = c[j], c[i]
		return self.output


if __name__ == '__main__':
	sln = Solution([1, 2, 3])
	print(sln.shuffle())
	print(sln.reset())
	print(sln.shuffle())
