from utils import TreeNode, binary_tree


class Solution:

	def isValidBST(self, root: TreeNode):

		def check(node, min_, max_):
			if not node:
				return True
			if node.val <= min_ or node.val >= max_:
				return False
			return (check(node.left, min_, node.val) and
			        check(node.right, node.val, max_))

		return check(root, float("-inf"), float("inf"))


if __name__ == '__main__':
	print(Solution().isValidBST(binary_tree([2, 1, 3])))
	print(Solution().isValidBST(binary_tree([10, 5, 15, None, None, 6, 20])))
	print(Solution().isValidBST(binary_tree([3, 1, 5, 0, 2, 4, 6, None, None, None, 3])))
