import collections
from typing import List


class Solution:

	def majorityElement(self, nums: List[int]) -> int:
		"""用字典记录出现的次数"""
		return collections.Counter(nums).most_common(1)[0][0]


if __name__ == '__main__':
	print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
	print(Solution().majorityElement([3, 2, 3]))
