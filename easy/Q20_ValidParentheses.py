from utils import benckmark


class Solution:

	def isValid(self, s: str) -> bool:
		"""
		将 pairs.values() 保存为变量，耗时降低了 0.18 秒/十万次
		"""
		pairs = {")": "(", "]": "[", "}": "{"}
		lefts, stack = pairs.values(), []
		for c in s:
			if c in lefts:
				stack.append(c)
			elif not stack or pairs[c] != stack.pop():
				return False
		return not stack


if __name__ == '__main__':
	print(Solution().isValid(""))
	print(Solution().isValid("()[]{}"))
	print(Solution().isValid("{[()]}"))
	print(Solution().isValid("([)]"))
	print(Solution().isValid("]"))

	benckmark(Solution().isValid, "()()(){}{}{}[][][]((({{{[[[]]]}}}))]{}{}", number=10_0000)
