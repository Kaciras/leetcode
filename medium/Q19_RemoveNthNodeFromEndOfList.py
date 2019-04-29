class Solution:
	"""
	一趟扫描 + 原地删除

	先将起始节点向后移动n+1个，并创建指向头的nth指针。然后继续遍历并移动当前指针和nth指针，遍历结束
	后nth指针即为倒数第n+1位置的节点，替换其next即可
	"""

	def removeNthFromEnd(self, head, n):
		"""
		:type head: ListNode
		:type n: int
		:rtype: ListNode
		"""
		node = head
		for i in range(n + 1):
			if not node: # 没有倒数第n+1项，说明删除的是链表头
				return head.next
			node = node.next

		nth = head

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
