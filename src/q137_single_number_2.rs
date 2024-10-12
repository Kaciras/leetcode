pub struct Solution {}

impl Solution {
	// 利用位最大为 1，三个的就是 3 可以用取余去除。
	pub fn single_number(nums: Vec<i32>) -> i32 {
		let mut result = 0;
		for i in 0..32 {
			let mut s = 0;
			for n in &nums {
				s += (n >> i) & 1;
			}
			result |= (s % 3) << i;
		}
		return result;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::single_number(vec![2, 2, 3, 2]), 3);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::single_number(vec![0, 1, 0, 1, 0, 1, 99]), 99);
	}
}
