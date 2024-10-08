from typing import Optional


class ListNode[T]:

	def __init__(self, x: T, next_=None):
		self.val: T = x
		self.next: Optional[ListNode[T]] = next_

	def __str__(self):
		# 链表可能有环，所以不能在此方法内打印全部节点
		if self.next:
			t = str(self.val) + " -> " + str(self.next.val)
		else:
			t = str(self.val) + "[E]"

		return f"{t}({self.length()})"

	def __repr__(self):
		return str(self)

	def length(self):
		"""
		获取该节点及其之后的节点数。 注意不能定义__len__，因为判断语句会调用而导致爆栈。
		"""
		node, visited = self, set()
		length = 0
		while node and node not in visited:
			visited.add(node)
			length += 1
			node = node.next
		return length


def linked_list(values: list) -> ListNode:
	head_, previous = None, None
	for v in values:
		node = ListNode(v)
		if previous:
			previous.next = node
		else:
			head_ = node
		previous = node
	return head_


def linked_list_factory(values):
	return lambda: linked_list(values)


def node_to_list(node: Optional[ListNode]):
	"""链表必须无环"""
	result = []
	while node:
		result.append(node.val)
		node = node.next
	return result


def print_linked_list(node: ListNode):
	"""
	在控制台上打印链表，与 LeetCode 的格式相同。
	"""
	visited = set()

	while node:
		if node in visited:
			print(f"{node.val}(环)")
			return
		visited.add(node)
		print(node.val, end="")
		node = node.next
		if node:
			print(" -> ", end="")

	print()  # 一般不会在同一行加什么了，可以换行。
