pub struct Solution;

impl Solution {
	pub fn jump(nums: Vec<i32>) -> i32 {
		let mut turn = 0;
		let mut s = 0;
		let mut e = 0;
		loop {
			if e >= nums.len() - 1 {
				return turn;
			}
			turn += 1;
			let next_s = e;
			for i in s..=e {
				e = e.max(i + nums[i] as usize);
			}
			s = next_s;
		}
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::jump(vec![2, 3, 1, 1, 4]), 2);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::jump(vec![2, 3, 0, 1, 4]), 2);
	}

	#[test]
	fn case1() {
		assert_eq!(Solution::jump(vec![0]), 0);
	}

	#[test]
	fn test1() {
		assert_eq!(Solution::jump(vec![1, 1, 1, 1, 99]), 4);
	}

	#[test]
	fn test2() {
		assert_eq!(Solution::jump(vec![99, 1, 1, 1, 1]), 1);
	}
}
