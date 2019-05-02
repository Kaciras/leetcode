from utils import linked_list, ListNode

class Solution:

	def mergeTwoLists(self, l1, l2):
		"""
		链表与数组不同：
		注意到直接设置next指针即意味着将链表的元素全部追加上去，故在
		其中一个链表剩余元素为0时可以直接将另一个追加到尾部
		"""
		prev_head = node = ListNode(None)

		while l1 and l2:
			if l1.val > l2.val:
				node.next, l2 = l2, l2.next
			else:
				node.next, l1 = l1, l1.next
			node = node.next

		if l1:
			node.next = l1
		if l2:
			node.next = l2

		return prev_head.next

	def mergeTwoLists2(self, l1, l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		node, n0, n1 = ListNode(None), l1, l2
		prev_head = node

		while n0 or n1:
			if not n0 or (n1 and n0.val > n1.val):
				node.next, n1 = n1, n1.next
			else:
				node.next, n0 = n0, n0.next
			node = node.next

		return prev_head.next


if __name__ == '__main__':
	print(Solution().mergeTwoLists(linked_list([1, 2, 4]), linked_list([1, 3, 4])))
	print(Solution().mergeTwoLists(linked_list([1]), linked_list([])))
