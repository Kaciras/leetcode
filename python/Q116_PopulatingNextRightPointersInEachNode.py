from typing import Optional

from utils import binary_tree


class Node:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None


class Solution:
	"""
	两种方案，这里用 1，但似乎 2 性能更高。
	1）递归子树，每个连接左右，以及左子树的最右和右子树的最左。
	2）跟 102 题一样做分层递归，连接每一层内的即可。
	"""

	def connect(self, root: 'Optional[Node]'):
		if not root:
			return
		left, right = root.left, root.right
		while left:
			left.next = right
			left, right = left.right, right.left
		self.connect(root.left)
		self.connect(root.right)

		return root  # 新版要求返回了，原来不要的。


if __name__ == '__main__':
	t = binary_tree([1, 2, 3, 4, 5, 6, 7])
	Solution().connect(t)
	print(t)
