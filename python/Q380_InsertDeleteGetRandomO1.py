import random

from utils import serial_call


# 我 TM 竟然想不到数组跟最后一个元素交换即可 O(1) 时间删除，可能是太长时间不写代码脑子生锈了
class RandomizedSet:

	def __init__(self):
		self.map = {}
		self.array = []

	def insert(self, val: int) -> bool:
		if val in self.map:
			return False
		self.map[val] = len(self.array)
		self.array.append(val)
		return True

	# dict.pop() 删除并返回被删除的值。
	def remove(self, val: int) -> bool:
		if val not in self.map:
			return False

		i = self.map.pop(val)
		tail = self.array.pop()

		# 如果删除的是末尾，则不用交换。
		if i != len(self.array):
			self.map[tail] = i
			self.array[i] = tail

		return True

	# random.choice 挺方便的哦，虽然空集合会出异常
	def getRandom(self) -> int:
		return random.choice(self.array) if self.array else None


if __name__ == '__main__':
	serial_call(
		["RandomizedSet", "remove", "remove", "insert", "getRandom", "remove", "insert"],
		[[], [0], [0], [0], [], [0], [0]]
	)
	serial_call(
		["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
		[[], [1], [2], [2], [], [1], [2], []]
	)
