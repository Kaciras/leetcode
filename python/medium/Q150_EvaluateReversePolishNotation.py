class Solution:
	"""
	operator 库包含了基本运算符的函数，但没有 int(a / b)，
	注意 int(a / b) 不等于 a // b。
	"""

	operators = {
		"+": lambda a, b: b + a,
		"-": lambda a, b: b - a,
		"*": lambda a, b: b * a,
		"/": lambda a, b: int(b / a),
	}

	def evalRPN(self, tokens: list[str]):
		stack = []
		for t in tokens:
			f = self.operators.get(t)
			if f:
				a = stack.pop()
				b = stack.pop()
				stack.append(f(a, b))
			else:
				stack.append(int(t))
		return stack[0]


if __name__ == '__main__':
	print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
	print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
