from utils import linked_list, ListNode, print_linked_list


class Solution:
	"""从运行时间来看，先转整数再转回链表反而更快"""

	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		head = node = ListNode(0)
		carry = 0

		while l1 or l2:
			v1 = v2 = 0
			if l1:
				v1, l1 = l1.val, l1.next
			if l2:
				v2, l2 = l2.val, l2.next

			sum_ = carry + v1 + v2
			if sum_ > 9:
				sum_, carry = sum_ - 10, 1
			else:
				carry = 0
			node.next = ListNode(sum_)
			node = node.next

		if carry == 1:
			node.next = ListNode(1)

		return head.next


if __name__ == '__main__':
	print_linked_list(Solution().addTwoNumbers(linked_list([0]), linked_list([9])))
	print_linked_list(Solution().addTwoNumbers(linked_list([2, 4, 3]), linked_list([5, 6, 4])))
	print_linked_list(Solution().addTwoNumbers(linked_list([9, 9, 9]), linked_list([1])))
