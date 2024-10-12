import itertools

from pytest_unordered import unordered


class Solution:

	def permute(self, nums: list[int]):
		if len(nums) == 1:
			return [nums]
		result = []
		for i, n in enumerate(nums):
			r = self.permute(nums[:i] + nums[i + 1:])
			for sub in r:
				sub.append(n)
				result.append(sub)
		return result

	def permute_1(self, nums):
		"""内置库刚好有干这事的"""
		return list(itertools.permutations(nums))


def test_example1():
	assert Solution().permute([1, 2, 3]) == unordered([
		[1, 2, 3],
		[1, 3, 2],
		[2, 1, 3],
		[2, 3, 1],
		[3, 1, 2],
		[3, 2, 1],
	])

def test_example2():
	assert Solution().permute([0, 1]) == unordered([[0, 1], [1, 0]])


def test_example3():
	assert Solution().permute([1]) == [[1]]
