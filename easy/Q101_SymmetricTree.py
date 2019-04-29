from utils import TreeNode, binary_tree


class Solution:

	def isSymmetric(self, root):
		"""
		队列果然比递归慢
		:type root: TreeNode
		:rtype: bool
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
