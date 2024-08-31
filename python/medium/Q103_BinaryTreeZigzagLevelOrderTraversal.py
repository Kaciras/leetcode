from utils import TreeNode, binary_tree


class Solution:
	"""此题直接 N % 2 == 0 判断还快些"""

	def zigzagLevelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []

		queue, next_ = [root], []
		result, reverse = [], True

		while queue:
			row = []
			for p in reversed(queue):
				row.append(p.val)
				if reverse:
					if p.left: next_.append(p.left)
					if p.right: next_.append(p.right)
				else:
					if p.right: next_.append(p.right)
					if p.left: next_.append(p.left)

			result.append(row)
			queue.clear()
			queue, next_, reverse = next_, queue, not reverse

		return result


if __name__ == '__main__':
	print(Solution().zigzagLevelOrder(binary_tree([3, 9, 20, None, None, 15, 7])))
