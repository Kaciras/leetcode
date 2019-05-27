from utils import linked_list, ListNode, print_linked_list

class Solution:

	def deleteNode(self, node: ListNode) -> None:
		node.val = node.next.val
		node.next = node.next.next


if __name__ == '__main__':
	head = linked_list([4, 5, 1, 9])
	Solution().deleteNode(head)
	print_linked_list(head)
