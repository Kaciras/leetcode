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


if __name__ == '__main__':
	print(Solution().generateParenthesis(2))
	print(Solution().generateParenthesis(3))
	print(Solution().generateParenthesis(4))
