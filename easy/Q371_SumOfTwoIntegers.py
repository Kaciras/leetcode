class Solution:
	"""乘除运算和sum()函数底层也使用了加减法，故不应使用"""

	def getSum(self, a, b):
		"""
		纯位运算实现
		:type a: int
		:type b: int
		:rtype: int
		"""

		def add(x, y):
			sum_, i, c = 0, 0, 0
			while (x != 0 or y != 0) and i < 32:
				bit, c = (x ^ y ^ c) & 1, (x & y) | (x & c) | (y & c)
				sum_ |= bit << i
				i += 1
				x, y = x >> 1, y >> 1
			sum_ |= (c & 1) << i
			return sum_ & 0xFFFFFFFF

		# Python 的整数只有long，需要手动实现溢出
		r = add(a, b)
		if r > 0x7FFFFFFF:
			r = -add(r ^ 0xFFFFFFFF, 1)
		return r


if __name__ == '__main__':
	print(Solution().getSum(3, 5))
	print(Solution().getSum(-3, 5))
	print(Solution().getSum(-123, 50))

	print(Solution().getSum(-2 ** 31, -1))
	print(Solution().getSum(2 ** 31 - 1, 1))
