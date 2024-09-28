from utils import TreeNode, tree_to_list


class Solution:
	"""
	思路是三个节点一组来看，通过中序遍历来确定前序的下一个的位置。
	前序：[本节点，左，右]
	中序：[左，本节点，右]
	"""

	preorder: list
	inorder: list
	map: dict[TreeNode, int]
	index = 0

	def buildTree(self, preorder: list, inorder: list):
		self.preorder = preorder
		self.inorder = inorder
		self.map = {i: v for v, i in enumerate(inorder)}
		return self.recursive(0, len(inorder))

	def recursive(self, lo: int, hi: int):
		if self.index == len(self.preorder):
			return None

		val = self.preorder[self.index]
		node, k = TreeNode(val), self.map[val]

		# 按前序遍历顺序扫描，中序定位。
		self.index += 1

		# 中序列表里，该节点左侧有元素，说明前序的接下来是左节点
		if k > lo:
			node.left = self.recursive(lo, k)

		# 中序列表里，该节点右侧有元素，说明前序的接下来是右节点
		if k < hi - 1:
			node.right = self.recursive(k + 1, hi)

		return node


if __name__ == '__main__':
	x = Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
	print(tree_to_list(x))
	x = Solution().buildTree([-1], [-1])
	print(tree_to_list(x))
	x = Solution().buildTree([1, 2, 4, 6, 5, 7, 8, 3, 9], [4, 6, 2, 7, 5, 8, 1, 9, 3])
	print(tree_to_list(x))
