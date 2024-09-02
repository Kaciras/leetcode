pub struct Solution {}

impl Solution {
	pub fn is_palindrome(x: i32) -> bool {
		if x < 0 {
			return false;
		}
		if x == 0 {
			return true;
		}
		let mut i = 10i32.pow(x.ilog10());
		let mut j = 1_i32;

		while i > j {
			let right = x / j % 10;
			let left = x / i % 10;
			if left != right {
				return false;
			}
			i /= 10;
			j *= 10;
		}
		return true;
	}

	// 转字符串比较是最简单的，面试紧张的话可以先说这种。
	pub fn is_palindrome_1(x: i32) -> bool {
		let a = x.to_string();
		return a.chars().eq(a.chars().rev());
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::is_palindrome(121), true);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::is_palindrome(-121), false);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::is_palindrome(10), false);
	}

	#[test]
	fn test1() {
		assert_eq!(Solution::is_palindrome(0), true);
	}
}
