import random


# 我 TM 竟然想不到数组跟最后一个元素交换即可O(1)时间删除，可能是太长时间不写代码脑子生锈了
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

	# dict.pop() 删除并返回被删除的值
	# 第一次忘了更新map里的索引
	def remove(self, val: int) -> bool:
		if val not in self.map:
			return False
		i = self.map.pop(val)
		tail = self.array[i] = self.array[-1]
		self.array.pop()
		self.map[tail] = i
		return True

	# random.choice 挺方便的哦，虽然空集合会出异常
	def getRandom(self) -> int:
		return random.choice(self.array) if self.array else None


if __name__ == '__main__':
	obj = RandomizedSet()
	print(obj.insert(1))
	print(obj.remove(2))
	print(obj.insert(2))
	print(obj.getRandom())
	print(obj.remove(1))
	print(obj.insert(2))
	print(obj.getRandom())
