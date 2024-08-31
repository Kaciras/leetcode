from typing import List

from utils import TreeNode


class Solution:

	def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
		"""
		更优的方法是不使用切片，而是使用索引来分隔左右两部分
		"""
		middle = len(nums) // 2
		root = TreeNode(nums[middle])
		root.left = self.sortedArrayToBST(nums[:middle])
		root.right = self.sortedArrayToBST(nums[middle + 1:])
		return root


if __name__ == '__main__':
	e = Solution().sortedArrayToBST([-10, -3, 0, 5, 9])
