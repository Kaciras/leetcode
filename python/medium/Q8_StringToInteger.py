class Solution:

	def myAtoi(self, s: str) -> int:
		s = s.lstrip()
		if len(s) == 0:
			return 0
		i, r, signum = 0, 0, 1

		if s[0] == "-":
			i, signum = 1, -1
		elif s[0] == "+":
			i = 1

		while i < len(s):
			v = ord(s[i]) - 48 # 48 换为 ord("0") 更可读
			if not 0 <= v < 10:
				break # 可以换用 isdigit()
			i += 1
			r = r * 10 + v

		r *= signum

		return max(-2 ** 31, min(r, 2 ** 31 - 1))


if __name__ == '__main__':
	print(Solution().myAtoi("  -0012a42"))
	print(Solution().myAtoi("+1"))
	print(Solution().myAtoi("       -42"))
	print(Solution().myAtoi("4193 with words"))
	print(Solution().myAtoi("words and 987"))
	print(Solution().myAtoi("-91283472332"))
