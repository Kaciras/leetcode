class Solution:
	def trailingZeroes(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		d, zeros = 5, 0
		while n >= d:
			zeros += n // d
			d *= 5
		return zeros

if __name__ == '__main__':
	print(Solution().trailingZeroes(1000))
