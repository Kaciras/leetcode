pub struct Solution;

// Rust 正好自带该功能……说实话二分搜索写烂了，我也懒得搞这题。
impl Solution {
	pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
		return nums.binary_search(&target).unwrap_or_else(|e| e) as i32;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 5), 2);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 2), 1);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::search_insert(vec![1, 3, 5, 6], 7), 4);
	}
}
