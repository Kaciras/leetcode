pub struct Solution {}

// 由于子数组连续，所以扫描范围也得是连续的区间，即滑动窗口。
impl Solution {
	pub fn min_sub_array_len(target: i32, nums: Vec<i32>) -> i32 {
		let mut length = usize::MAX;
		let mut sum = nums[0];
		let mut left = 0;
		let mut right = 1;
		while left < right {
			if sum < target {
				if right == nums.len() {
					break;
				}
				sum += nums[right];
				right += 1;
			} else {
				length = length.min(right - left);
				sum -= nums[left];
				left += 1;
			}
		}
		return if length == usize::MAX { 0 } else { length as i32 };
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::min_sub_array_len(7, vec![2, 3, 1, 2, 4, 3]), 2);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::min_sub_array_len(4, vec![1, 4, 4]), 1);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::min_sub_array_len(11, vec![1, 1, 1, 1, 1, 1, 1, 1]), 0);
	}

	#[test]
	fn user1() {
		assert_eq!(Solution::min_sub_array_len(11, vec![0]), 0);
	}

	#[test]
	fn user2() {
		assert_eq!(Solution::min_sub_array_len(11, vec![11]), 1);
	}
}
