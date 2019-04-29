from utils import TreeNode, binary_tree


class Solution:
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
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
	print(Solution().inorderTraversal(binary_tree([1, None, 2, None, None, 3])))
