use std::collections::HashSet;

pub struct Solution;

impl Solution {
	pub fn is_happy(mut n: i32) -> bool {
		let mut seen = HashSet::new();
		seen.insert(n);

		while n != 1 {
			let mut value = 0;
			while n > 0 {
				let d = n % 10;
				n = n / 10;
				value += d * d;
			}
			n = value;
			if (!seen.insert(value)) {
				return false;
			}
		}
		return true; // 平方相加最多 81 * 9，不会溢出。
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::is_happy(19), true);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::is_happy(2), false);
	}

	#[test]
	fn case1() {
		assert_eq!(Solution::is_happy(0), false);
	}

	#[test]
	fn case2() {
		assert_eq!(Solution::is_happy(1), true);
	}
}
