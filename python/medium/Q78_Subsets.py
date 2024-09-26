import itertools

class Solution:

	def subsets(self, nums: list[int]):
		"""总之基本思路就是递归，写法上可以分几轮循环"""
		result = [[]]
		for i in nums:
			result.extend([c + [i] for c in result])
		return result

	def subsets_1(self, nums: list[int]):
		result = [nums]
		for i in range(0, len(nums)):
			result.extend(itertools.combinations(nums, i))
		return result


if __name__ == '__main__':
	print(Solution().subsets([]))
	print(Solution().subsets([1, 2, 3]))
