from utils import TreeNode, binary_tree


class Solution:
	def kthSmallest(self, root, k):
		"""
		:type root: TreeNode
		:type k: int
		:rtype: int
		"""
		self.remain = k
		self.result = None

		def LDR(node):
			if self.remain > 0 and node:
				LDR(node.left)
				self.remain -= 1
				if self.remain == 0:
					self.result = node.val
				LDR(node.right)

		LDR(root)
		return self.result


if __name__ == '__main__':
	print(Solution().kthSmallest(binary_tree([3, 1, 4, None, 2]), 1))
	print(Solution().kthSmallest(binary_tree([5, 3, 6, 2, 4, None, None, 1]), 3))
