class Solution:
	"""就是二分搜索，只不过相等时有两种不同的处理情况"""

	def searchRange(self, nums: list[int], target: int):

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

		start = bs(0, len(nums), True)
		end = bs(0, len(nums), False) - 1

		return [-1, -1] if end < start else [start, end]


def test_example1():
	assert Solution().searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]


def test_example2():
	assert Solution().searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, - 1]


def test_example3():
	assert Solution().searchRange([], 1) == [-1, - 1]
