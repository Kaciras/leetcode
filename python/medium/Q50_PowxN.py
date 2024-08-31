class Solution:
	def myPow(self, x, n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""
		if n == 0:
			return 1
		negative, result = n < 0, 1
		n = abs(n)

		while n > 0:
			base, p = x, 2
			while p < n:
				base *= base
				p *= 2
			result *= base
			n -= p // 2

		return 1 / result if negative else result


if __name__ == '__main__':
	print(Solution().myPow(-2.0, 9))
	print(Solution().myPow(0.00001, 2147483647))

	print(Solution().myPow(2.0, 10))
	print(Solution().myPow(2.10000, 3))
	print(Solution().myPow(2.00000, -2))

