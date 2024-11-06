use crate::linked_list::ListNode;

pub struct Solution;

// 这里直接比较合并，复杂度 N * K，使用二分堆的话可以降到 Nlog(K) 时间。
impl Solution {
	pub fn merge_k_lists(mut lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
		let mut previous = Some(Box::new(ListNode { val: 0, next: None }));
		let mut node = &mut previous;

		lists.retain(|v| v.is_some());

		while lists.len() > 0 {
			let mut i = Self::min_index(&lists);
			let mut n = lists[i].take();
			let g = n.as_mut().unwrap().next.take();
			let mut x = node.as_mut().unwrap();
			x.next = n;
			node = &mut x.next;

			if g.is_none() {
				lists.remove(i);
			} else {
				lists[i] = g;
			}
		}
		return previous.unwrap().next;
	}

	fn min_index(lists: &Vec<Option<Box<ListNode>>>) -> usize {
		let mut min = i32::MAX;
		let mut index = usize::MAX;
		for i in 0..lists.len() {
			let v = lists[i].as_ref().unwrap().val;
			if v < min {
				min = v;
				index = i;
			}
		}
		return index;
	}
}

#[cfg(test)]
mod tests {
	use super::*;
	use crate::linked_list::assert_list_eq;

	#[test]
	fn example1() {
		let input = vec![
			ListNode::from_list(&[1, 4, 5]),
			ListNode::from_list(&[1, 3, 4]),
			ListNode::from_list(&[2, 6]),
		];
		let output = Solution::merge_k_lists(input);
		assert_list_eq(&output, &[1, 1, 2, 3, 4, 4, 5, 6]);
	}

	#[test]
	fn example2() {
		assert_list_eq(&Solution::merge_k_lists(vec![]), &[]);
	}

	#[test]
	fn example3() {
		assert_list_eq(&Solution::merge_k_lists(vec![None]), &[]);
	}
}
