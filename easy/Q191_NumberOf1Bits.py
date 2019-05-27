class Solution(object):
	"""这题没有PY3，不能加类型定义"""

	def hammingWeight(self, n):
		"""Python 自带一个直接转二进制字符串的函数"""
		return bin(n).count("1")

	def hammingWeight2(self, n):
		count = 0
		while n > 0:
			if n & 1 == 1:
				count += 1
			n >>= 1
		return count


if __name__ == '__main__':
	print(Solution().hammingWeight(11)) # 3
	print(Solution().hammingWeight(128)) # 1
	print(Solution().hammingWeight(2147483648)) # 1
