pub struct Solution;

impl Solution {
	pub fn first_missing_positive(mut nums: Vec<i32>) -> i32 {
		// 它内部使用的是跟 Q27 一样的末尾交换法。
		nums.retain(|&x| x > 0);

		// 使用负数来标记该位置的正数已存在。
		for i in 0..nums.len() {
			let k = nums[i].abs() as usize - 1;
			if k < nums.len() && nums[k] > 0 {
				nums[k] *= -1;
			}
		}

		// 找到第一个正数，如果没有则为 nums 的长度。
		return 1 + nums.iter()
			.position(|&x| x > 0)
			.unwrap_or(nums.len()) as i32;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn case1() {
		assert_eq!(Solution::first_missing_positive(vec![1]), 2);
	}

	#[test]
	fn case2() {
		assert_eq!(Solution::first_missing_positive(vec![0]), 1);
	}

	#[test]
	fn case3() {
		assert_eq!(Solution::first_missing_positive(vec![1, 1]), 2);
	}

	#[test]
	fn example1() {
		assert_eq!(Solution::first_missing_positive(vec![1, 2, 0]), 3);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::first_missing_positive(vec![3, 4, -1, 1]), 2);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::first_missing_positive(vec![7, 8, 9, 11, 12]), 1);
	}
}
