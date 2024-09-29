from utils import TreeNode


class Solution:

	def sortedArrayToBST(self, nums: list[int]):
		"""
		更快的方法是不使用切片，而是使用索引来分隔左右两部分
		"""
		if not nums: return None

		i = len(nums) // 2
		node = TreeNode(nums[i])

		node.left = self.sortedArrayToBST(nums[:i])
		node.right = self.sortedArrayToBST(nums[i + 1:])
		return node


if __name__ == '__main__':
	print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))
