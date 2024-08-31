from utils import linked_list, benckmark


class Solution:
	"""这题没有Py3，不能在参数上定义类型"""

	def getIntersectionNode(self, ha, hb):
		"""
		先求出两个链表的长度，以及它们的差，然后让长的先跑长度差个，
		再两个一起跑，此时它们一定会在交点处相遇，或是同时到达尾部。
		"""

		ca, cb = self.length(ha), self.length(hb)
		if ca > cb:
			ha = self.next_of(ha, ca - cb)
		else:
			hb = self.next_of(hb, cb - ca)

		while ha:
			if ha == hb: return ha
			ha, hb = ha.next, hb.next

		return None

	def length(self, head):
		r = 0
		while head:
			r += 1
			head = head.next
		return r

	def next_of(self, node, n):
		for i in range(n):
			node = node.next
		return node


if __name__ == '__main__':
	a, b, c = linked_list(["a1", "a2"]), \
			  linked_list(["b1", "b2", "b3"]), \
			  linked_list(["c1", "c2", "c3"])
	a.next.next = b.next.next.next = c
	print(Solution().getIntersectionNode(a, b))

	benckmark(Solution().getIntersectionNode, a, b, ratio=1)
