use std::collections::HashMap;

pub struct Solution;

impl Solution {
	pub fn contains_nearby_duplicate(nums: Vec<i32>, k: i32) -> bool {
		let mut map = HashMap::new();
		let k = k as usize;
		for (i, x) in nums.into_iter().enumerate() {
			if let Some(j) = map.insert(x, i) {
				if j + k >= i {
					return true;
				}
			}
		}
		return false;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert!(Solution::contains_nearby_duplicate(vec![1, 2, 3, 1], 3));
	}

	#[test]
	fn example2() {
		assert!(Solution::contains_nearby_duplicate(vec![1, 0, 1, 1], 1));
	}

	#[test]
	fn example3() {
		assert!(!Solution::contains_nearby_duplicate(vec![1, 2, 3, 1, 2, 3], 2));
	}
}
