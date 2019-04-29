from utils import linked_list, ListNode, print_linked_list


class Solution:
	def hasCycle(self, head):
		"""
		:type head: ListNode
		:rtype: bool
		"""
		slow = fast = head
		while fast:
			slow, fast = slow.next, fast.next
			if not fast:
				return False
			fast = fast.next
			if fast == slow:
				return True
		return False


if __name__ == '__main__':
	a = ListNode(0)
	b = ListNode(1)
	c = ListNode(2)
	d = ListNode(3)

	a.next = b
	b.next = c
	c.next = d
	d.next = b

	print_linked_list(a)
	print(Solution().hasCycle(a))
	d.next = None
	print(Solution().hasCycle(a))
