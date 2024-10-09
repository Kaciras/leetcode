from utils import ListNode, linked_list, node_to_list


class Solution:
	"""
	一趟扫描 + 原地删除：
	1) 将起始节点向后移动 n+1 个，并创建指向头的 nth 指针，俩指针同步移动。
	2) 继续遍历并移动当前指针和 nth 指针，
	3) 结束后 nth 指针即为倒数第 n+1 位置的节点，替换其 next 即可
	"""

	def removeNthFromEnd(self, head: ListNode, n: int):
		node = nth = head
		for i in range(n + 1):
			# 没有倒数第 n+1 项，说明删的是头
			if not node:
				return head.next
			node = node.next

		while node:
			nth = nth.next
			node = node.next

		nth.next = nth.next.next
		return head



def test_example1():
	assert node_to_list(Solution().removeNthFromEnd(linked_list([1, 2, 3, 4, 5]), 2)) == [1, 2, 3, 5]


def test_example2():
	assert node_to_list(Solution().removeNthFromEnd(linked_list([1, 2]), 1)) == [1]


def test_example3():
	assert node_to_list(Solution().removeNthFromEnd(linked_list([1]), 1)) == []
