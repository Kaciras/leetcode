import itertools

class Solution:

	def subsets(self, nums):
		result = [[]]
		for i in nums:
			result.extend([c + [i] for c in result])
		return result

	def subsets_old(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		result = [nums]
		for i in range(0, len(nums)):
			result.extend(itertools.combinations(nums, i))
		return result


if __name__ == '__main__':
	print(Solution().subsets([]))
	print(Solution().subsets([1, 2, 3]))
