use std::fmt::{Display, Write};

#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
	pub val: i32,
	pub next: Option<Box<ListNode>>,
}

impl ListNode {
	// 傻屄 Rust 不支持默认参数，非得起一大堆函数名。
	#[inline]
	fn create(val: i32, next: Option<Box<ListNode>>) -> Self {
		ListNode { next, val }
	}

	#[inline]
	fn new(val: i32) -> Self {
		ListNode { next: None, val }
	}

	pub fn from_list(values: &[i32]) -> Option<Box<Self>> {
		return values.iter().rev()
			.fold(None, |n, v| Some(Box::new(ListNode::create(*v, n))));
	}
}

pub fn node_to_vec(node: &Option<Box<ListNode>>) -> Vec<i32> {
	let mut vec = Vec::new();
	let mut x = node;
	while let Some(n) = x {
		x = &n.next;
		vec.push(n.val);
	}
	return vec;
}

pub fn assert_list_eq(head: &Option<Box<ListNode>>, expected: &[i32]) {
	assert_eq!(node_to_vec(head).as_slice(), expected);
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn create_empty() {
		assert_eq!(ListNode::from_list(&[]), None);
	}

	#[test]
	fn create() {
		let head = ListNode::from_list(&[11, 22]);
		assert_eq!(head.as_ref().unwrap().val, 11);
		assert_eq!(head.unwrap().next.unwrap().val, 22);
	}

	#[test]
	fn to_vec() {
		let head = ListNode::from_list(&[11, 22]);
		assert_eq!(node_to_vec(&head), vec![11, 22]);
	}

	#[test]
	fn assert_list_eq_0() {
		assert_list_eq(&ListNode::from_list(&[]), &[])
	}

	#[test]
	fn assert_list_eq_1() {
		assert_list_eq(&ListNode::from_list(&[11, 22]), &[11, 22])
	}
}
