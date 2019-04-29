"""
辅助模块，包含构建链表、二叉树，打印数据结构到控制台等便捷方法
"""
import collections


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


# 二叉树

class TreeNode:

	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	def __repr__(self):
		return str(self.val)


def binary_tree(values):
	"""
	根据列表创建二叉树
	:param values: 节点值的列表,其中None值代表节点不存在
	:return: 树的根节点
	:rtype: TreeNode
	"""
	if not values:
		return None

	root = TreeNode(values[0])
	queue, leave = collections.deque(), collections.deque(values[1:])
	queue.append(root)

	def next_node():
		"""封装了判断节点是否存在的逻辑"""
		if not leave:
			return None
		v = leave.popleft()
		return None if v is None else TreeNode(v)

	def not_null(*args):
		return filter(lambda x: x is not None, args)

	while queue:
		node = queue.popleft()
		if not node:
			continue
		node.left = next_node()
		node.right = next_node()
		queue.extend(not_null(node.left, node.right))

	return root

def print_binart_tree(node):
	pass

def print_martix(martix):
	print("[")
	for row in martix:
		print("\t[" + ", ".join(map(str, row)) + "]")
	print("]")


def not_null(iterable):
	return filter(lambda x: x is not None, iterable)