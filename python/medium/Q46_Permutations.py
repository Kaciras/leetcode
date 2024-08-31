import itertools


class Solution:

	def permute_manual(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		if len(nums) == 1:
			return [nums]
		result = []
		for i, n in enumerate(nums):
			r = self.permute_manual(nums[:i] + nums[i + 1:])
			for per in r:
				result.append(per)
				per.append(n)
		return result

	def permute(self, nums):
		"""内置库刚好有干这事的"""
		return list(itertools.permutations(nums))


if __name__ == '__main__':
	print(Solution().permute_manual([1, 2]))
	print(Solution().permute_manual([1, 2, 3]))
