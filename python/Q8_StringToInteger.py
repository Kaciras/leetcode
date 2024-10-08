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
			v = ord(s[i]) - 48  # 48 换为 ord("0") 更可读
			if not 0 <= v < 10:
				break  # 可以换用 isdigit()
			i += 1
			r = r * 10 + v

		r *= signum

		return max(-2 ** 31, min(r, 2 ** 31 - 1))


def test_example1():
	assert Solution().myAtoi("42") == 42


def test_example2():
	assert Solution().myAtoi("-042") == -42


def test_example3():
	assert Solution().myAtoi("1337c0d3") == 1337


def test_example4():
	assert Solution().myAtoi("0-1") == 0


def test_example5():
	assert Solution().myAtoi("words and 987") == 0


def test_case1():
	assert Solution().myAtoi("4193 with words") == 4193


def test_case2():
	assert Solution().myAtoi("-91283472332") == -2147483648


def test_case3():
	assert Solution().myAtoi("       -42") == -42
