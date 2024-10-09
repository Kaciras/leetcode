from utils import benckmark, node_to_list
from utils import linked_list, ListNode, linked_list_factory


class Solution:

	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		"""
		链表与数组不同：
		注意到直接设置 next 指针即意味着将链表的元素全部追加上去，
		故在其中一个链表剩余元素为 0 时可以直接将另一个追加到尾部。
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


def _invoke(l1: list[int], l2: list[int]):
	return node_to_list(Solution().mergeTwoLists(linked_list(l1), linked_list(l2)))


def test_example1():
	assert _invoke([1, 2, 4], [1, 3, 4]) == [1, 1, 2, 3, 4, 4]


def test_example2():
	assert _invoke([], []) == []


def test_example3():
	assert _invoke([], [0]) == [0]


if __name__ == '__main__':
	a = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 23, 29, 31, 37, 41]
	b = [0, 2, 8, 12, 13, 14, 15, 16, 20, 21, 22, 30, 35, 39, 42, 45, 50, 51, 100, 200, 300, 400, 1000, 1024, 2048]
	benckmark(Solution().mergeTwoLists, linked_list_factory(a), linked_list_factory(b), ratio=0.1)
