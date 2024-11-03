pub struct Solution;

impl Solution {
	pub fn add_binary(a: String, b: String) -> String {
		let a = a.as_bytes();
		let b = b.as_bytes();

		let mut result = Vec::new();
		let mut carry = 0;
		for i in 0..a.len().max(b.len()) {
			let x = if i < a.len() { a[a.len() - i - 1] - b'0' } else { 0 };
			let y = if i < b.len() { b[b.len() - i - 1] - b'0' } else { 0 };

			let z = x + y + carry;
			carry = z >> 1;
			result.push((z & 1) + b'0')
		}

		if carry == 1 {
			result.push(b'1');
		}
		result.reverse();
		return unsafe { String::from_utf8_unchecked(result) };
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::add_binary("11".into(), "1".into()), "100");
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::add_binary("1010".into(), "1011".into()), "10101");
	}

	#[test]
	fn user1() {
		assert_eq!(Solution::add_binary("0".into(), "0".into()), "0");
	}
}
