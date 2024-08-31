import random


class Solution:
	"""也可以保存两个数组来避免每次都复制一份"""

	def __init__(self, nums):
		"""
		:type nums: List[int]
		"""
		self.nums = nums

	def reset(self):
		"""
		Resets the array to its original configuration and return it.
		:rtype: List[int]
		"""
		return self.nums

	def shuffle(self):
		"""
		Returns a random shuffling of the array.
		:rtype: List[int]
		"""
		r = self.nums.copy()
		for i in range(len(r) - 1, 0, -1):
			j = random.randint(0, i)
			r[i], r[j] = r[j], r[i]
		return r


if __name__ == '__main__':
	Solution([1, 2, 3]).shuffle()
