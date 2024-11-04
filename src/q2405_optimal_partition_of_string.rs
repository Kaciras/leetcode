pub struct Solution;

// 只有 bool 两种状态时可以考虑用位图。
impl Solution {
	pub fn partition_string(s: String) -> i32 {
		let s = s.as_bytes();
		let mut seen = 0u32;
		let mut substrings = 1;

		for c in s {
			let i = 1 << (c - b'a');
			if seen & i != 0 {
				seen = 0;
				substrings += 1;
			}
			seen |= i;
		}
		return substrings;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::partition_string("abacaba".into()), 4);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::partition_string("ssssss".into()), 6);
	}
}
