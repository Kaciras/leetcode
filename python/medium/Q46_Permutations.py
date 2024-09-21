import itertools


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


if __name__ == '__main__':
	print(Solution().permute([1, 2]))
	print(Solution().permute([1, 2, 3]))
