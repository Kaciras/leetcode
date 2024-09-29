from utils import TreeNode, binary_tree


class Solution:

	def inorderTraversal(self, root: TreeNode):
		"""前序遍历"""
		result = []
		self.LDR(root, result)
		return result

	def LDR(self, node: TreeNode, result: list):
		if node is None:
			return
		self.LDR(node.left, result)
		result.append(node.val)
		self.LDR(node.right, result)

	def inorderTraversal_1(self, root: TreeNode):
		result, stack = [], []

		while root or stack:
			while root:
				stack.append(root)
				root = root.left
			root = stack.pop()
			result.append(root.val)
			root = root.right

		return result


if __name__ == '__main__':
	sln = Solution()
	print(sln.inorderTraversal(binary_tree([1, None, 2, 3])))  # [1, 3, 2]
	print(sln.inorderTraversal(binary_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9])))  # [4, 2, 6, 5, 7, 1, 3, 9, 8]
	print(sln.inorderTraversal(binary_tree([])))  # []
	print(sln.inorderTraversal(binary_tree([1])))  # [1]
