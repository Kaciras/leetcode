from utils import TreeNode, binary_tree


class Solution:
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		result = []

		def DLR(node, depth):
			if not node:
				return
			if len(result) < depth:
				result.append([])
			result[depth - 1].append(node.val)
			DLR(node.left, depth + 1)
			DLR(node.right, depth + 1)

		DLR(root, 1)
		return result


if __name__ == '__main__':
	print(Solution().levelOrder(binary_tree([3, 9, 20, None, None, 15, 7])))
