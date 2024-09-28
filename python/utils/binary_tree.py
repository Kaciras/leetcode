import collections
import math
from collections import deque
from typing import Optional


def not_null(*args):
	return filter(lambda x: x is not None, args)


class TreeNode[T]:

	def __init__(self, x: T):
		self.val = x
		self.left: Optional[TreeNode[T]] = None
		self.right: Optional[TreeNode[T]] = None

	def __repr__(self):
		return str(self.val)


def binary_tree(values: list) -> Optional[TreeNode]:
	"""
	根据列表创建二叉树，是 LeetCode 的常见操作。

	:param values: 节点值的列表,其中 None 值代表节点不存在
	:return: 根节点，如果输入是空列表则返回 None
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


def tree_to_list(root: TreeNode):
	"""跟 LeetCode 一样的树转列表，分层遍历"""
	queue, output = deque(), []
	queue.append(root)

	while queue:
		node = queue.popleft()
		if not node:
			output.append(None)
			continue
		output.append(node.val)
		queue.append(node.left)
		queue.append(node.right)

	# 最后会多一层全空，这里计算深度来去除。
	depth = int(math.log2(len(output)))
	return output[:2 ** depth - 1]
