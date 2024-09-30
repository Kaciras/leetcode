class Solution:
	"""这题是 Medium 但实际上只有 Easy 难度"""

	chars = [None, None, "abc", "def",
	         "ghi", "jkl", "mno",
	         "pqrs", "tuv", "wxyz"]

	def letterCombinations(self, digits: str) -> list[str]:
		if len(digits) == 0:
			return []
		if len(digits) == 1:
			return list(self.chars[int(digits)])

		c = self.chars[int(digits[0])]
		comb = self.letterCombinations(digits[1:])

		return [x + y for x in c for y in comb]


if __name__ == '__main__':
	print(Solution().letterCombinations("2"))
	print(Solution().letterCombinations("234"))