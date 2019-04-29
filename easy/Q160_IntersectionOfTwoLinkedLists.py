from utils import linked_list, ListNode, print_linked_list


class Solution:
	def getIntersectionNode(self, headA, headB):
		"""
		:type headA: ListNode
		:type headB: ListNode
		:rtype: ListNode
		"""
		def count(head):
			r = 0
			while head:
				r += 1
				head = head.next
			return r

		def next_of(node, n):
			for i in range(n):
				node = node.next
			return node

		countA, countB = count(headA), count(headB)
		if countA > countB:
			headA = next_of(headA, countA - countB)
		else:
			headB = next_of(headB, countB - countA)

		while headA:
			if headA == headB:
				return headA
			headA, headB = headA.next, headB.next
		return None


if __name__ == '__main__':
	a, b, c = linked_list(["a1", "a2"]), \
			  linked_list(["b1", "b2", "b3"]), \
			  linked_list(["c1", "c2", "c3"])
	a.next.next = b.next.next.next = c
	print(Solution().getIntersectionNode(a, b))
