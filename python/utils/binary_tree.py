import collections
from typing import Optional


def not_null(*args):
	return filter(lambda x: x is not None, args)


class TreeNode:

	def __init__(self, x):
		self.val = x
		self.left: Optional[TreeNode] = None
		self.right: Optional[TreeNode] = None

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
