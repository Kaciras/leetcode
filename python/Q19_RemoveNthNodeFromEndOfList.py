from utils import ListNode


class Solution:
	"""
	一趟扫描 + 原地删除

	先将起始节点向后移动 n+1 个，并创建指向头的 nth 指针。然后继续遍历并移动当前指针和 nth 指针，遍历结束
	后 nth 指针即为倒数第 n+1 位置的节点，替换其 next 即可
	"""

	def removeNthFromEnd(self, head: ListNode, n: int):
		node = nth = head
		for i in range(n + 1):
			node = node.next

		# 没有倒数第 n+1 项，说明删的是头
		if not node:
			return head.next

		while node:
			nth = nth.next
			node = node.next

		nth.next = nth.next.next
		return head


if __name__ == '__main__':
	import utils.common as util

	print(Solution().removeNthFromEnd(util.linked_list([1, 2, 3, 4, 5]), 2))
	print(Solution().removeNthFromEnd(util.linked_list([1, 5]), 1))
	print(Solution().removeNthFromEnd(util.linked_list([1, 5]), 2))
