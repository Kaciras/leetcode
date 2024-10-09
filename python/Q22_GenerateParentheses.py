class Solution:
	"""建立二叉树模型，分析路径比较容易理解"""

	def generateParenthesis(self, n: int):
		result = []

		def generate(left, right, pars):
			if left == right == 0:
				return result.append(pars)
			if left > right:
				return
			if left > 0:
				generate(left - 1, right, pars + "(")
			if right > 0:
				generate(left, right - 1, pars + ")")

		generate(n, n, "")
		return result


def test_example1():
	assert Solution().generateParenthesis(3) == ["((()))", "(()())", "(())()", "()(())", "()()()"]


def test_example2():
	assert Solution().generateParenthesis(1) == ["()"]
