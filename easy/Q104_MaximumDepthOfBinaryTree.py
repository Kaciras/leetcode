class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None


class Solution:
	"""一个DFS完事"""

	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if not root:
			return 0
		return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
