from utils import TreeNode


class Solution:
	"""一个DFS完事"""

	def maxDepth(self, root: TreeNode) -> int:
		if not root:
			return 0
		return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
