from utils import invoker

"""
如果是生产环境，用 Python 自带的 OrderedDict 即可实现。
原理是把字典和双向链表结合起来，每次获取时将节点挪到最前，淘汰最后的节点。
"""


class ListNode:
	__slots__ = ("key", "value", "prev", "next")

	def __init__(self, k, v):
		self.key = k
		self.value = v
		self.prev = None
		self.next = None


class LinkedList:
	"""可以的优化：用虚拟节点作为首尾"""

	def __init__(self):
		self.head = None
		self.tail = None

	def add_first(self, node: ListNode):
		if not self.head:
			self.head = self.tail = node
		else:
			node.prev, node.next = None, self.head
			node.next.prev = self.head = node

	def remove(self, node: ListNode):
		if node == self.tail:
			self.remove_last()
		elif node == self.head:
			self.remove_first()
		else:
			node.prev.next = node.next
			node.next.prev = node.prev

	def remove_first(self):
		node = self.head

		if node == self.tail:
			self.head = self.tail = None
		else:
			self.head = node.next
			node.next.prev = None

		return node

	def remove_last(self):
		node = self.tail

		if node == self.head:
			self.head = self.tail = None
		else:
			self.tail = node.prev
			node.prev.next = None

		return node


class LRUCache:

	def __init__(self, capacity: int):
		self.capacity = capacity
		self.dict = {}
		self.list = LinkedList()

	def get(self, key: int) -> int:
		if key in self.dict.keys():
			return self._get_and_refresh(key).value
		return -1

	def put(self, key: int, value: int) -> None:
		if key in self.dict.keys():
			self._get_and_refresh(key).value = value
		else:
			if len(self.dict) >= self.capacity:
				del self.dict[self.list.remove_last().key]
			node = ListNode(key, value)
			self.dict[key] = node
			self.list.add_first(node)

	def _get_and_refresh(self, key):
		node = self.dict[key]
		self.list.remove(node)
		self.list.add_first(node)
		return node


if __name__ == '__main__':
	invoker.serial_call(
		["LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get",
		 "put", "put", "put", "get", "put", "get", "get", "get", "get", "put", "put", "get",
		 "get", "get", "put", "put", "get", "put", "get", "put", "get", "get", "get", "put",
		 "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put", "put",
		 "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put",
		 "put", "get", "put", "put", "get", "put", "get", "get", "get", "put", "get", "get",
		 "put", "put", "put", "put", "get", "put", "put", "put", "put", "get", "get", "get",
		 "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put", "get",
		 "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put",
		 "put", "put"],
		[[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25],
		 [8], [9, 22], [5, 5], [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9],
		 [10], [10], [6, 14], [3, 1], [3], [10, 11], [8], [2, 14], [1], [5], [4], [11, 4],
		 [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5], [2, 9], [13, 4],
		 [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22],
		 [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4],
		 [1], [10], [3, 29], [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26],
		 [8], [7], [5], [13, 17], [2, 27], [11, 15], [12], [9, 19], [2, 15], [3, 16], [1],
		 [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7], [5, 2], [9, 28], [1], [2, 2],
		 [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]
	)
