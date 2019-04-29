class Solution:
	def myAtoi(self, str):
		"""
		:type str: str
		:rtype: int
		"""
		str = str.lstrip()
		if len(str) == 0:
			return 0
		i, r, signum = 0, 0, 1

		if str[0] == "-":
			i, signum = 1, -1
		elif str[0] == "+":
			i = 1

		while i < len(str):
			v = ord(str[i]) - 48 # 48换为ord("0")更可读
			if not 0 <= v < 10:
				break # 可以换用isdigit()
			r = r * 10 + v
			i += 1
		r *= signum

		if r > 2 ** 31 - 1:
			return 2 ** 31 - 1
		if r < -2 ** 31:
			return -2 ** 31
		return r


if __name__ == '__main__':
	print(Solution().myAtoi("  -0012a42"))
	print(Solution().myAtoi("+1"))
	print(Solution().myAtoi("       -42"))
	print(Solution().myAtoi("4193 with words"))
	print(Solution().myAtoi("words and 987"))
	print(Solution().myAtoi("-91283472332"))
