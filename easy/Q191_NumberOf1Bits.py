class Solution(object):
	"""return bin(x ^ y).count("1") 这个最骚"""

	def hammingWeight(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		count = 0
		while n > 0:
			if n & 1 == 1:
				count += 1
			n >>= 1
		return count


if __name__ == '__main__':
	print(Solution().hammingWeight(11))
	print(Solution().hammingWeight(128))
	print(Solution().hammingWeight(2147483648))
