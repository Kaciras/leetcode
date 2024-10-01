from typing import Optional

from utils import TreeNode, binary_tree


class Solution:
	"""BST 中序遍历就是从小到大，计数到第 N 个即可"""

	remain: int
	result: Optional[int]

	def kthSmallest(self, root: TreeNode, k: int):
		self.remain = k
		self.result = None
		self.LDR(root)
		return self.result

	def LDR(self, node):
		if self.remain == 0 or node is None:
			return
		self.LDR(node.left)
		self.remain -= 1
		if self.remain == 0:
			self.result = node.val
		self.LDR(node.right)


if __name__ == '__main__':
	print(Solution().kthSmallest(binary_tree([3, 1, 4, None, 2]), 1))
	print(Solution().kthSmallest(binary_tree([5, 3, 6, 2, 4, None, None, 1]), 3))
