from typing import List


class Solution:

	def singleNumber(self, nums: List[int]) -> int:
		result = 0
		for n in nums:
			result ^= n
		return result


if __name__ == '__main__':
	print(Solution().singleNumber([2, 2, 1]))  # 1
	print(Solution().singleNumber([4, 1, 2, 1, 2]))  # 1
