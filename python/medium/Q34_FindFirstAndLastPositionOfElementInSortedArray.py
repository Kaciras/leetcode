class Solution:
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		def bs(lo, hi, on_equal_left):
			if lo == hi:
				return lo
			mid = (lo + hi) >> 1
			if target > nums[mid]:
				return bs(mid + 1, hi, on_equal_left)
			if target < nums[mid]:
				return bs(lo, mid, on_equal_left)
			if on_equal_left:
				return bs(lo, mid, on_equal_left)
			else:
				return bs(mid + 1, hi, on_equal_left)

		start, end = bs(0, len(nums), True), bs(0, len(nums), False) - 1
		if end < start:
			return [-1, -1]
		return [start, end]


if __name__ == '__main__':
	print(Solution().searchRange(nums=[], target=1))
	print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
	print(Solution().searchRange(nums=[5, 7, 7, 8, 8, 10], target=6))
