from utils import benckmark

pairs = {")": "(", "]": "[", "}": "{"}


class Solution:

	def isValid(self, s: str) -> bool:
		"""
		将 pairs.values() 保存为变量，耗时降低了 1.8 秒/百万次
		"""
		lefts, stack = pairs.values(), []
		for c in s:
			if c in lefts:
				stack.append(c)
			elif not stack or pairs[c] != stack.pop():
				return False
		return not stack


def test_example1():
	assert Solution().isValid("()") == True


def test_example2():
	assert Solution().isValid("()[]{}") == True


def test_example3():
	assert Solution().isValid("(]") == False


def test_example4():
	assert Solution().isValid("([])") == True


def test_case1():
	assert Solution().isValid("") == True


def test_case2():
	assert Solution().isValid("([)]") == False


def test_case3():
	assert Solution().isValid("]") == False


if __name__ == '__main__':
	benckmark(Solution().isValid, "()()(){}{}{}[][][]((({{{[[[]]]}}}))]{}{}", ratio=0.1)
