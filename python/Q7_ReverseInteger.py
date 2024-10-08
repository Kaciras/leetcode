class Solution:
	"""两种方法：字符串翻转法，个位相加法"""

	def reverse(self, x: int) -> int:
		v, n = 0, abs(x)
		while n > 0:
			v = (v * 10) + (n % 10)
			n //= 10
		if v.bit_length() > 31:
			return 0
		return v if x > 0 else -v

	def reverse2(self, x: int) -> int:
		v = str(x)[::-1]
		v = -int(v[:-1]) if x < 0 else int(v)
		return v if v.bit_length() < 32 else 0


def test_example1():
	assert Solution().reverse(123) == 321


def test_example2():
	assert Solution().reverse(-123) == -321


def test_example3():
	assert Solution().reverse(120) == 21


def test_case1():
	assert Solution().reverse(1534236469) == 9646324351
