class Solution:
	"""注意此题不能用对数来做，因为存在精度损失"""

	def isPowerOfThree(self, n):
		"""
		:type n: int
		:rtype: bool
		"""
		return n > 0 and 1162261467 % n == 0


if __name__ == '__main__':
	print(Solution().isPowerOfThree(3))
	print(Solution().isPowerOfThree(27))
	print(Solution().isPowerOfThree(5))
	print(Solution().isPowerOfThree(0))
	print(Solution().isPowerOfThree(243))
