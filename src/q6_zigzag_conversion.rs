pub struct Solution {}

impl Solution {
	pub fn convert(s: String, num_rows: i32) -> String {
		if num_rows == 1 {
			return s;
		}
		let mut output = String::with_capacity(s.len());
		for row in 0..num_rows as usize {
			let mut i = row;
			while i < s.len() {
				if row < (num_rows as usize) -1 {
					output.push(s.chars().nth(i).unwrap());
					i += 2 * (num_rows as usize - row) - 2;
				}
				if i >= s.len() {
					break;
				}
				if row > 0 {
					output.push(s.chars().nth(i).unwrap());
					i += row * 2;
				}
			}
		}
		return output;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		let output = Solution::convert("PAYPALISHIRING".into(), 3);
		assert_eq!(output, "PAHNAPLSIIGYIR");
	}

	#[test]
	fn example2() {
		let output = Solution::convert("PAYPALISHIRING".into(), 4);
		assert_eq!(output, "PINALSIGYAHRPI");
	}

	#[test]
	fn example3() {
		let output = Solution::convert("PAYPALISHIRING".into(), 1);
		assert_eq!(output, "PAYPALISHIRING");
	}
}
