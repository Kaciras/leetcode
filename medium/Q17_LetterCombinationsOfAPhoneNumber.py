class Solution:
	chars = [None, None, "abc", "def",
			 "ghi", "jkl", "mno",
			 "pqrs", "tuv", "wxyz"]

	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if len(digits) == 0:
			return []
		if len(digits) == 1:
			return list(self.chars[int(digits)])

		cs, co = self.chars[int(digits[0])], self.letterCombinations(digits[1:])
		return [x + y for x in cs for y in co]


if __name__ == '__main__':
	print(Solution().letterCombinations("2"))
	print(Solution().letterCombinations("234"))
