from utils import linked_list, ListNode, print_linked_list


class Solution:
	def oddEvenList(self, head):
		"""
		:type head: ListNode
		:rtype: ListNode
		"""
		if not head:
			return
		odd, even, bound, prev = head, head.next, head.next, None
		while odd and even:
			odd.next = odd.next.next if odd.next else None
			prev, odd = odd, odd.next
			even.next = even.next.next if even.next else None
			even = even.next
		(odd if odd else prev).next = bound
		return head


def test(input_):
	ll = linked_list(input_)
	Solution().oddEvenList(ll)
	print_linked_list(ll)


if __name__ == '__main__':
	test([])
	test([1, 2, 3, 4, 5])
	test([2, 1, 3, 5, 6, 4, 7])
	test([1])
	test([1,2])
	test([1, 3, 2, 4])
