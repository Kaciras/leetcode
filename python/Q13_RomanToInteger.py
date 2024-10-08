class Solution:
	table = {
		"I": 1, "V": 5, "X": 10, "L": 50,
		"C": 100, "D": 500, "M": 1000,
	}

	def romanToInt(self, s: str) -> int:
		"""反向遍历更方便"""
		table = self.table
		result = last = 0

		for n in reversed(s):
			c = table[n]
			if c >= last:
				result += c
				last = c
			else:
				result -= c

		return result

	def romanToInt2(self, s: str) -> int:
		"""利用数字能够做减法来抵消上次加法的特点"""
		last, result = float("inf"), 0

		for n in s:
			current = self.table[n]
			if last >= current:
				result += current
				last = current
			else:
				result += current - last - last  # 把上次的减掉
				last = float("inf")

		return result


def test_example1():
	assert Solution().romanToInt("III") == 3


def test_example2():
	assert Solution().romanToInt("LVIII") == 58


def test_example3():
	assert Solution().romanToInt("MCMXCIV") == 1994
