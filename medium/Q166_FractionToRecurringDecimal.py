class Solution:
	"""divmod() 同时计算商和余数"""

	def fractionToDecimal(self, num, den):
		"""
		:type num: int
		:type den: int
		:rtype: str
		"""
		negative = (num < 0) ^ (den < 0)
		result, num = divmod(abs(num), abs(den))
		decimal, visited, i = "", dict(), 0

		while num != 0:
			if num in visited.keys():
				start = visited[num]
				decimal = decimal[:start] + "(" + decimal[start:] + ")"
				break
			visited[num] = i
			i += 1
			s, num = divmod(num * 10, den)
			decimal += str(s)

		result = str(result)
		if decimal:
			result = result + "." + decimal
		if negative and result != "0":
			result = "-" + result
		return result

if __name__ == '__main__':
	print(Solution().fractionToDecimal(-50, 8))
	print(Solution().fractionToDecimal(-1, 7))
	print(Solution().fractionToDecimal(0, -1))
	print(Solution().fractionToDecimal(0, 1))
	print(Solution().fractionToDecimal(1, 2))
	print(Solution().fractionToDecimal(2, 1))
	print(Solution().fractionToDecimal(2, 3))
	print(Solution().fractionToDecimal(1, 7))
