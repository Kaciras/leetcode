pub struct Solution;

// 第一次写的时候竟然忘了三角形要两边和大于第三边。
impl Solution {
	pub fn triangle_type(nums: Vec<i32>) -> String {
		let a = nums[0];
		let b = nums[1];
		let c = nums[2];
		if a + b <= c || a + c <= b || b + c <= a {
			return String::from("none");
		}
		return match (a == b, a == c, b == c) {
			(true, true, true) => String::from("equilateral"),
			(false, false, true) => String::from("isosceles"),
			(true, false, false) => String::from("isosceles"),
			(false, true, false) => String::from("isosceles"),
			_ => String::from("scalene"),
		};
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::triangle_type(vec![3, 3, 3]), String::from("equilateral"));
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::triangle_type(vec![3, 4, 5]), String::from("scalene"));
	}

	#[test]
	fn test1() {
		assert_eq!(Solution::triangle_type(vec![3, 4, 3]), String::from("isosceles"));
	}

	#[test]
	fn test2() {
		assert_eq!(Solution::triangle_type(vec![8, 4, 2]), String::from("none"));
	}
}
