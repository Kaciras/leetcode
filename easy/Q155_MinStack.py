class MinStack:
	"""用stack里的值与最小值的差来记录上次最小值"""

	def __init__(self):
		self.stack = []
		self.mininum = None

	def push(self, x: int):
		if not self.stack:
			self.stack.append(x)
			self.mininum = x
		else:
			self.stack.append(x - self.mininum)
			if x < self.mininum:
				self.mininum = x

	def pop(self) -> int:
		if not self.stack:
			return self.mininum
		v = self.stack.pop()
		if v < 0:
			self.mininum -= v

	def top(self) -> int:
		if len(self.stack) == 1:
			return self.mininum
		v = self.stack[-1]
		if v > 0:
			return v + self.mininum
		return self.mininum

	def getMin(self) -> int:
		return self.mininum


if __name__ == '__main__':
	obj = MinStack()
	obj.push(1)
	obj.push(2)
	# obj.push(-3)
	print(obj.top())
	print(obj.getMin())
	obj.pop()
	print(obj.getMin())
	print(obj.top())
