from utils import linked_list, ListNode, benckmark


class Solution:

	def isPalindrome(self, head: ListNode) -> bool:
		"""
		先快慢指针找出中间的（奇数）或中点的下一个（偶数），然后从它开始反序后面一半，最后比较两部分即可
		"""
		slow = fast = head
		while fast and fast.next:
			slow, fast = slow.next, fast.next.next

		pre, length = None, 0
		while slow:
			slow.next, pre, slow = pre, slow, slow.next

		# 这里必须用后半作为循环条件，因为前半可能最后还连着后半的第一个
		while pre:
			if head.val != pre.val:
				return False
			head, pre = head.next, pre.next

		return True

	def isPalindrome_1(self, head: ListNode) -> bool:
		"""计数法找中间的节点，效率不高"""
		size, node = 0, head
		while node:
			size += 1
			node = node.next
		middle = size // 2

		node, prev, index = head, None, 0
		while index < middle:
			node.next, prev, node = prev, node, node.next
			index += 1

		if size & 1 != 0:
			node = node.next

		while node:
			if node.val != prev.val:
				return False
			node, prev = node.next, prev.next
		return True


if __name__ == '__main__':
	print(Solution().isPalindrome(linked_list([1])))
	print(Solution().isPalindrome(linked_list([8, 0, 8])))
	print(Solution().isPalindrome(linked_list([])))
	print(Solution().isPalindrome(linked_list([1, 2, 2, 1])))
	print(Solution().isPalindrome(linked_list([1, 2, 2, 3])))

	arg = linked_list([16, 1, 2, 8, 7, 5, 5, 6, 20, 0, 20, 6, 5, 5, 7, 8, 2, 1, 16])
	benckmark(Solution().isPalindrome, arg, ratio=1)
