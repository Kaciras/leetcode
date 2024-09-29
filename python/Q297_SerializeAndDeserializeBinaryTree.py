import ast
from collections import deque

from utils import TreeNode, binary_tree


class Codec:

	def serialize(self, root):
		"""Encodes a tree to a single string.

		:type root: TreeNode
		:rtype: str
		"""
		if not root:
			return []
		queue, result, end = deque([root]), [], 0
		while queue:
			node = queue.popleft()
			if node:
				result.append(node.val)
				queue.extend((node.left, node.right))
				end = len(result)
			else:
				result.append(None)

		return str(result[:end])

	def deserialize(self, data):
		"""Decodes your encoded data to tree.

		:type data: str
		:rtype: TreeNode
		"""
		if not data:
			return None

		data = ast.literal_eval(data.replace("null", "None"))
		root, queue, leave = TreeNode(data[0]), deque(), deque(data[1:])
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


tree = binary_tree([5, 4, 7, 3, None, 2, None, -1, None, 9])
codec = Codec()
x = codec.serialize(tree)
print(x)
r = codec.deserialize(x)
print(r)
