# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
	return [False, False, False, True, True, True, True][version]


class Solution:
	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		l, mid = 1, (1 + n) // 2
		while l < n:
			if isBadVersion(mid):
				n, mid = mid, (l + mid) // 2
			else:
				l, mid = mid + 1, (n + mid) // 2
		return n


if __name__ == '__main__':
	print(Solution().firstBadVersion(5))
