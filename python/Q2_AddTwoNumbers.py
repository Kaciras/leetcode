from utils import linked_list, ListNode, print_linked_list


class Solution:

	def linklist_to_int(self, node: ListNode):
		value, scale = 0, 1
		while node:
			value += node.val * scale
			scale *= 10
			node = node.next
		return value

	def int_to_linklist(self, value: int):
		head = node = ListNode(0)
		if value == 0:
			return head
		while value != 0:
			node.next = ListNode(value % 10)
			node, value = node.next, value // 10
		return head.next

	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
		"""方法 2，转整数相加，再转回链表"""
		v1 = self.linklist_to_int(l1)
		v2 = self.linklist_to_int(l2)
		return self.int_to_linklist(v1 + v2)

	def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
		"""方法 1，直接按位相加"""
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
	print_linked_list(Solution().addTwoNumbers(linked_list([0]), linked_list([9])))  # 9
	print_linked_list(Solution().addTwoNumbers(linked_list([0]), linked_list([0])))  # 0
	print_linked_list(Solution().addTwoNumbers(linked_list([2, 4, 3]), linked_list([5, 6, 4])))  # 7 -> 0 -> 8
	print_linked_list(Solution().addTwoNumbers(linked_list([9, 9, 9]), linked_list([1])))  # 0 -> 0 -> 0 -> 1