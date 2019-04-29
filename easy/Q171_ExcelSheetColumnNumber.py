class Solution:
	def titleToNumber(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		result, redix = 0, 1
		for ch in s[::-1]:
			result += (ord(ch) - 64) * redix
			redix *= 26
		return result


if __name__ == '__main__':
	print(Solution().titleToNumber("AB"))
	print(Solution().titleToNumber("ZY"))
