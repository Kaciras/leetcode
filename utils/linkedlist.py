class ListNode:

	def __init__(self, x):
		self.val = x
		self.next = None

	def __str__(self):
		# 链表可能有环，所以不能再此方法内打印全部节点
		if self.next:
			return str(self.val) + " -> " + str(self.next.val)
		return str(self.val) + "(End)"

	def __repr__(self):
		return str(self)


def linked_list(values):
	head_, previous = None, None
	for v in values:
		node = ListNode(v)
		if previous:
			previous.next = node
		else:
			head_ = node
		previous = node
	return head_


def print_linked_list(node):
	"""
	在控制台上打印链表
	:type node: ListNode
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
	print()
