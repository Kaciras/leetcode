class Solution:
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		v = str(x)[::-1]
		v = -int(v[:-1]) if x < 0 else int(v)
		return v if 2 ** 31 > v >= -2 ** 31 else 0 # 还可以用bit_length()

if __name__ == '__main__':
	print(Solution().reverse(123))
	print(Solution().reverse(-123))
	print(Solution().reverse(120))
	print(Solution().reverse(1534236469))
