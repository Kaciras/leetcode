from pytest import approx

class Solution:
	"""每次直接翻倍，指数减半，比每次都乘底数更快"""

	def myPow(self, x: float, n: int):
		if n == 0:
			return 1

		neg, result, n = n < 0, 1, abs(n)

		while n > 0:
			base, p = x, 2
			while p < n:
				base *= base
				p *= 2
			result *= base
			n -= p // 2

		return 1 / result if neg else result


def test_case1():
	assert Solution().myPow(0.00001, 2147483647) == 0


def test_example1():
	assert Solution().myPow(2.00000, 10) == 1024


def test_example2():
	assert Solution().myPow(2.10000, 3) == approx(9.261)


def test_example3():
	assert Solution().myPow(2.00000, -2) == 0.25000
