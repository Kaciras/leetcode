import utils.common as util

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution:
	def isPalindrome(self, head):
		"""
		比较暴力的算法，反序前半在挨个比较，能够达到要求的时空间复杂度，但是
		时间复杂度的常数项大
		:type head: ListNode
		:rtype: bool
		"""
		size, node = 0, head
		while node:
			size += 1
			node = node.next
		middle = size // 2

		node, prev, index = head, None, 0
		while index < middle:
			node.next, prev, node = prev, node, node.next
			index += 1
		# TODO: 上面两步可以用双指针一遍完成

		if size & 1 != 0:
			node = node.next

		while node:
			if node.val != prev.val:
				return False
			node, prev = node.next, prev.next
		return True


if __name__ == '__main__':
	print(Solution().isPalindrome(util.linked_list([1])))
	print(Solution().isPalindrome(util.linked_list([8, 0, 8])))
	print(Solution().isPalindrome(util.linked_list([])))
	print(Solution().isPalindrome(util.linked_list([1, 2, 2, 1])))
	print(Solution().isPalindrome(util.linked_list([1, 2, 2, 3])))
