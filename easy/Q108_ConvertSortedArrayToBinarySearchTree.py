from utils import TreeNode, binary_tree


class Solution:

	def sortedArrayToBST(self, nums):
		"""
		更优的方法是不适用切片，而是使用索引来分隔左右两部分
		:type nums: List[int]
		:rtype: TreeNode
		"""
		if not nums:
			return None
		middle = len(nums) // 2
		root = TreeNode(nums[middle])
		root.left = self.sortedArrayToBST(nums[:middle])
		root.right = self.sortedArrayToBST(nums[middle + 1:])
		return root


if __name__ == '__main__':
	e = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
	print()
