class MinStack:

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		self.stack = []
		self.mininum = None

	def push(self, x):
		"""
		:type x: int
		:rtype: void
		"""
		if not self.stack:
			self.stack.append(x)
			self.mininum = x
		else:
			self.stack.append(x - self.mininum)
			if x < self.mininum:
				self.mininum = x

	def pop(self):
		"""
		:rtype: void
		"""
		if not self.stack:
			return self.mininum
		v = self.stack.pop()
		if v < 0:
			self.mininum -= v

	def top(self):
		"""
		:rtype: int
		"""
		if len(self.stack) == 1:
			return self.mininum
		v = self.stack[-1]
		if v > 0:
			return v + self.mininum
		return self.mininum

	def getMin(self):
		"""
		:rtype: int
		"""
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
