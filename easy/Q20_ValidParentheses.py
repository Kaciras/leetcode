class Solution:
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		map_, stack = {")":"(", "]":"[", "}":"{"}, []
		for ch in s:
			if ch in map_.values():
				stack.append(ch)
			elif not stack or map_[ch] != stack.pop():
				return False
		return not stack


if __name__ == '__main__':
	print(Solution().isValid(""))
	print(Solution().isValid("()[]{}"))
	print(Solution().isValid("{[()]}"))
	print(Solution().isValid("([)]"))
	print(Solution().isValid("]"))