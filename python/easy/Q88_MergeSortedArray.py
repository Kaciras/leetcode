class Solution:

	def merge(self, nums1: list[int], m: int, nums2: list[int], n: int):
		"""
		关键是反向遍历，因为 nums1 的后面有空，所以不会干扰到 nums1 前面的数
		"""
		m, n, total = m - 1, n - 1, m + n - 1
		while m >= 0 and n >= 0:
			if nums1[m] < nums2[n]:
				nums1[total] = nums2[n]
				n -= 1
			else:
				nums1[total] = nums1[m]
				m -= 1
			total -= 1
		if n >= 0:
			nums1[:n + 1] = nums2[:n + 1]


def test(a, b):
	nums1 = [0] * (len(a) + len(b))
	nums1[:len(a)] = a
	nums1[len(a):] = [0] * len(b)
	Solution().merge(nums1, len(a), b, len(b))
	print(nums1)


if __name__ == '__main__':
	test([], [1])
	test([1], [])
	test([1, 2, 3, 9], [5, 6, 7])
	test([2], [1])
	test([1, 2, 4, 5, 6], [3])
