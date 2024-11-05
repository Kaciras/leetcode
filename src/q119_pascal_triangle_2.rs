pub struct Solution;

// 公式：C(n,k) = n!/k!(n−k)!，注意要用 long 型计算避免溢出。
impl Solution {
	pub fn get_row(n: i32) -> Vec<i32> {
		let mut result = Vec::with_capacity(n as usize + 1);
		result.push(1);

		let mut v = 1i64;
		for k in 1..=n as i64 {
			v = v * (n as i64 - k + 1) / k;
			result.push(v as i32);
		}
		return result;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::get_row(3), vec![1, 3, 3, 1]);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::get_row(0), vec![1]);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::get_row(1), vec![1, 1]);
	}

	#[test]
	fn test1() {
		assert_eq!(Solution::get_row(5), vec![1, 5, 10, 10, 5, 1]);
	}
}
