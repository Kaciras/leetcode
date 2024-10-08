import heapq


class Solution:
	"""正常做的话是搞堆结构"""

	def findKthLargest(self, nums: list[int], k: int):
		return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
	print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
	print(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
	print(Solution().findKthLargest([2, 1], 2))
