from utils import TreeNode, binary_tree, benckmark


class Solution:

	def isSymmetric(self, root: TreeNode) -> bool:
		"""把递归函数放外面比里面快了0.3秒/百万次"""
		if not root:
			return True
		return self.cmp(root.left, root.right)

	def cmp(self, left, right):
		if not left:
			return not right
		if not right:
			return not left
		return left.val == right.val and self.cmp(left.left, right.right) and self.cmp(left.right, right.left)


	def isSymmetric2(self, root: TreeNode) -> bool:
		"""
		队列比递归慢了
		"""
		if not root:
			return True
		lq, rq = [root.left], [root.right]

		while len(lq) > 0 and len(rq) > 0:
			l, r = lq.pop(), rq.pop()
			if l != r:
				if l is None or r is None :
					return False
				if l.val != r.val:
					return False
			if l:
				lq.append(l.left)
				lq.append(l.right)
			if r:
				rq.append(r.right)
				rq.append(r.left)

		return len(lq) == len(rq) == 0


if __name__ == '__main__':
	print(Solution().isSymmetric(binary_tree([1, 2, 2, 3, 4, 4, 3])))
	print(Solution().isSymmetric(binary_tree([1, 2, 2, None, 3, None, 3])))

	benckmark(Solution().isSymmetric, binary_tree([1, 2, 2, 3, 4, 4, 3]))
	# benckmark(Solution().isSymmetric2, binary_tree([1, 2, 2, 3, 4, 4, 3]))