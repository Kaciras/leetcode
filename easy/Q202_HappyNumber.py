class Solution:
	def isHappy(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		contains = set()
		while n not in contains:
			contains.add(n)
			n = sum(map(lambda x: x * x, map(int, str(n))))
			if n == 1:
				return True
		return False


if __name__ == '__main__':
	print(Solution().isHappy(0))
	print(Solution().isHappy(1))
	print(Solution().isHappy(19))
	print(Solution().isHappy(123456789))
