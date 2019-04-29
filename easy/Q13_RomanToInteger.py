class Solution:

	table = {
		"I": 1, "V": 5, "X": 10, "L": 50,
		"C": 100, "D": 500, "M": 1000
	}

	def romanToInt(self, s):
		"""利用数字能够做减法来抵消上次加法的特点"""
		last, result = float("inf"), 0
		for n in s:
			current = self.table[n]
			if last >= current:
				result += current
				last = current
			else:
				result += current - last - last # 把上次的减掉
				last = float("inf")
		return result

	def romanToInt_old(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		i = result = 0
		dec = False
		while i < len(s):
			temp = self.table[s[i]]
			i += 1
			if i < len(s):
				next_ = self.table[s[i]]
				if next_ > temp:
					result += next_ - temp
					i += 1
					continue
			result += temp
		return result

if __name__ == '__main__':
	print(Solution().romanToInt("III"))  # 3
	print(Solution().romanToInt("IV"))  # 4
	print(Solution().romanToInt("IX"))  # 9
	print(Solution().romanToInt("MCMXCIV"))  # 1994
