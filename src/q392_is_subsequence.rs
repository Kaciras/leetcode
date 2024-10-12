pub struct Solution {}

impl Solution {
	pub fn is_subsequence(s: String, t: String) -> bool {
		let s = s.as_bytes();
		let t = t.as_bytes();

		if s.is_empty() {
			return true;
		}

		let mut j = 0;
		for &c in t {
			if s[j] == c {
				j += 1;
			}
			if j == s.len() {
				return true;
			}
		}
		return false;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn case1() {
		assert_eq!(Solution::is_subsequence(String::from(""), String::from("ahbgdc")), true);
	}

	#[test]
	fn example1() {
		assert_eq!(Solution::is_subsequence(String::from("abc"), String::from("ahbgdc")), true);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::is_subsequence(String::from("axc"), String::from("ahbgdc")), false);
	}

	#[test]
	fn user1() {
		assert_eq!(Solution::is_subsequence(String::from("abc"), String::from("ab")), false);
	}

	#[test]
	fn user2() {
		assert_eq!(Solution::is_subsequence(String::from("abc"), String::from("abcd")), true);
	}

	#[test]
	fn user3() {
		assert_eq!(Solution::is_subsequence(String::from("fuck"), String::from("")), false);
	}
}
