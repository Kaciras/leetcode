pub struct Solution;

// 唯一要注意的是数字是从 1 开始的，每次要减一。
impl Solution {
	pub fn convert_to_title(mut column_number: i32) -> String {
		let mut result = Vec::new();
		while column_number != 0 {
			column_number -= 1;
			let v = column_number % 26;
			column_number = column_number / 26;
			result.push(65 + v as u8);
		}
		result.reverse();
		return String::from_utf8(result).unwrap();
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::convert_to_title(1), String::from("A"));
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::convert_to_title(28), String::from("AB"));
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::convert_to_title(701), String::from("ZY"));
	}
}
