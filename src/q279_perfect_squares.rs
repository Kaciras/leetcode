pub struct Solution;

// 这题挺没意思的，不知道这个定理就没法写出最佳实现，只能穷举。
impl Solution {

	// 四平方和定理: 任意一个正整数都可以被表示为至多四个正整数的平方和。
	// 且仅 n = 4k × (8m + 7) 时才是 4 个，其它情况为三个及以下。
	pub fn num_squares(mut n: i32) -> i32 {
		let v = n as f64;
		let b = v.sqrt().floor();

		// 1 个的情况，n 为完全平方数。
		if b * b == v {
			return 1;
		}

		// 4 个的情况，测试符合公式。
		while n % 4 == 0 {
			n /= 4;
		}
		if n % 8 == 7 {
			return 4;
		}

		// 2 个的情况，需要循环测试下。
		for i in 1..=b as i32 {
			let c = v - (i * i) as f64;
			let d = c.sqrt().floor();

			if d * d == c {
				return 2;
			}
		}
		return 3; // 最后只剩下三个的了。
	}

	// 穷举法，复杂度 n * sqrt(n)，超时了。
	pub fn num_squares_1(n: i32) -> i32 {
		let mut factors = Vec::new();
		for i in 1..=n {
			if i * i > n {
				break;
			}
			factors.push(i * i);
		}
		let mut r = i32::MAX;
		Self::recursive(&factors, n, 1, &mut r);
		return r;
	}

	fn recursive(factors: &Vec<i32>, n: i32, i: i32, r: &mut i32) {
		for f in factors.iter().rev() {
			let d = n - f;
			if (d < 0) {
				continue;
			}
			if d == 0 {
				*r = i.min(*r)
			}
			Self::recursive(factors, d, i + 1, r)
		}
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn case1() {
		assert_eq!(Solution::num_squares(1), 1);
	}

	#[test]
	fn case2() {
		assert_eq!(Solution::num_squares(2), 2);
	}

	#[test]
	fn case3() {
		assert_eq!(Solution::num_squares(7), 4);
	}

	#[test]
	fn example1() {
		assert_eq!(Solution::num_squares(12), 3);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::num_squares(13), 2);
	}
}

