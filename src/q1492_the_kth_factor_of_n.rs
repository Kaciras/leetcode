pub struct Solution;

impl Solution {
	// 注意到约数是对称的，中心是平方根。
	pub fn kth_factor(n: i32, mut k: i32) -> i32 {
		let m = (n as f64).sqrt();
		for i in 1..m as i32 {
			if n % i != 0 {
				continue;
			}
			k -= 1;
			if k == 0 {
				return i;
			}
		}
		for i in m as i32..=n {
			if n % i != 0 {
				continue;
			}
			k -= 1;
			if k == 0 {
				return i;
			}
		}
		return -1;
	}

	// O(n) 的解法可以说是毫无难度。
	pub fn kth_factor_1(n: i32, k: i32) -> i32 {
		return (1..=n)
			.filter(|i| n % i == 0)
			.skip(k as usize - 1)
			.next().unwrap_or(-1);
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::kth_factor(12, 3), 3);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::kth_factor(7, 2), 7);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::kth_factor(4, 4), -1);
	}
}
