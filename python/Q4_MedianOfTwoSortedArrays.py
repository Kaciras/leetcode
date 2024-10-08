MAX_INT, MIN_INT = 2147483647, -2147483648


class Solution:
	"""
	1.不要被题目的复杂度误导，log(m + n) 包含比他小的 log(min(m, n))
	2.Hard 题多半都考某个数学知识，不知道就没辙。
	"""

	def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
		n1, n2 = len(nums1), len(nums2)
		if n1 > n2:
			return self.findMedianSortedArrays(nums2, nums1)

		left, right, k = 0, n1, (n1 + n2 + 1) // 2

		while left < right:
			mid = left + (right - left) // 2

			if nums1[mid] < nums2[k - mid - 1]:
				left = mid + 1
			else:
				right = mid

		lmax1 = nums1[left - 1] if left > 0 else MIN_INT
		left2 = k - left
		lmax2 = nums2[left2 - 1] if left2 > 0 else MIN_INT

		if (n1 + n2) & 1 == 1:
			return max(lmax1, lmax2)

		rmin1 = nums1[left] if left < n1 else MAX_INT
		rmin2 = nums2[left2] if left2 < n2 else MAX_INT

		return (max(lmax1, lmax2) + min(rmin1, rmin2)) / 2


def test_example1():
	assert Solution().findMedianSortedArrays([1, 3], [2]) == 2


def test_example2():
	assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5


def test_case1():
	assert Solution().findMedianSortedArrays([5, 6], []) == 5.5


def test_case2():
	assert Solution().findMedianSortedArrays([], [7]) == 7


def test_case3():
	assert Solution().findMedianSortedArrays([1, 3, 5, 7, 9], [4, 5, 6, 7, 8, 10]) == 6


def test_case4():
	assert Solution().findMedianSortedArrays([1, 2, 3, 4], [5, 6, 7, 8]) == 4.5
