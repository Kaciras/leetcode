from utils import linked_list, ListNode, print_linked_list


class Solution:
	def reverseList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		prev = None
		while head:
			head.next, prev, head = prev, head, head.next
		return prev


if __name__ == '__main__':
	print_linked_list(Solution().reverseList(linked_list([1, 2, 3, 4, 5])))
	print_linked_list(Solution().reverseList(linked_list([1])))
	print_linked_list(Solution().reverseList(linked_list([])))
