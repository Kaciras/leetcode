import collections
import heapq


class Solution:
	def topKFrequent(self, nums, k):
		"""
		Counter()时间复杂度 O(n)，most_common()复杂度 O(nlogn)
		二分堆求TOP(K)复杂度 O(nlogk)
		:type nums: List[int]
		:type k: int
		:rtype: List[int]
		"""
		ctr = collections.Counter(nums)
		return heapq.nlargest(k, ctr, key=lambda x: ctr[x])


if __name__ == '__main__':
	print(Solution().topKFrequent([5, 5, 5], 0))
	print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))
	print(Solution().topKFrequent([1], 1))
