from utils import TreeNode, binary_tree
from collections import deque


class TreeLinkNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None


class Solution:

	def connect(self, root):
		if not root:
			return
		left, right = root.left, root.right
		while left:
			left.next = right
			left, right = left.right, right.left
		self.connect(root.left)
		self.connect(root.right)


if __name__ == '__main__':
	t = binary_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
	Solution().connect(t)
	print(t)
