import operator

class Solution:
	"""operator 库包含了基本运算符的函数"""

	operators = {
		"+": lambda a, b: b + a,
		"-": lambda a, b: b - a,
		"*": lambda a, b: b * a,
		"/": lambda a, b: int(b / a),
	}

	def evalRPN(self, tokens):
		"""
		:type tokens: List[str]
		:rtype: int
		"""
		stack = []
		for t in tokens:
			if t in self.operators.keys():
				stack.append(self.operators[t](stack.pop(), stack.pop()))
			else:
				stack.append(int(t))
		return stack[0]


if __name__ == '__main__':
	print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
	print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
