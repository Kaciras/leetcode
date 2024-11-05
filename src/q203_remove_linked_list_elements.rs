use crate::linked_list::ListNode;

pub struct Solution;

impl Solution {
	pub fn remove_elements(mut head: Option<Box<ListNode>>, val: i32) -> Option<Box<ListNode>> {
		// 创建一个指针，只想表头
		let mut p = &mut head;

		// Rust 编译器太垃圾，交换两个 Some 的顺序或者用 while + if 都不行。
		// 等明年 polonius 完成再学吧。
		loop {
			match p {
				None => {
					return head; // 无环链表必然会遍历到空节点。
				},
				Some(node) if node.val == val => {
					*p = node.next.take(); // 指针所指的内存用 next 覆盖。
				},
				Some(node) => {
					p = &mut node.next; // 指针指向下一个节点。
				},
			}
		}
	}
}

#[cfg(test)]
mod tests {
	use super::*;
	use crate::linked_list::assert_list_eq;

	#[test]
	fn example1() {
		let input = ListNode::from_list(&[1, 2, 6, 3, 4, 5, 6]);
		assert_list_eq(&Solution::remove_elements(input, 6), &[1, 2, 3, 4, 5]);
	}

	#[test]
	fn example2() {
		let input = ListNode::from_list(&[]);
		assert_list_eq(&Solution::remove_elements(input, 1), &[]);
	}

	#[test]
	fn example3() {
		let input = ListNode::from_list(&[7, 7, 7, 7]);
		assert_list_eq(&Solution::remove_elements(input, 7), &[]);
	}
}
