use std::collections::hash_map::Entry::{Occupied, Vacant};
use std::collections::HashMap;

pub struct Solution {}

// 这题跟 205 是一样的，只不过把字符换成了字符串。
impl Solution {
	pub fn word_pattern(pattern: String, s: String) -> bool {
		let mut pattern = pattern.as_bytes();
		let mut c2w = [""; 26];
		let mut w2c = HashMap::new();

		let mut k = 0;
		for word in s.split_whitespace() {
			if k == pattern.len() {
				return false;
			}

			let c = pattern[k] - b'a';
			let value = &mut c2w[c as usize];
			k += 1;
			if *value == "" {
				*value = word;
			} else if *value != word {
				return false;
			}

			// Rust 这个一次查询 + 更新的 API 比 C# 难用。
			match w2c.entry(word) {
				Vacant(v) => {
					v.insert(c);
				}
				Occupied(o) => {
					if *o.get() != c { return false; }
				}
			};
		}

		return k == pattern.len();
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn case1() {
		assert_eq!(Solution::word_pattern(String::from("abba"), String::from("dog dog dog dog")), false);
	}

	#[test]
	fn example1() {
		assert_eq!(Solution::word_pattern(String::from("abba"), String::from("dog cat cat dog")), true);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::word_pattern(String::from("abba"), String::from("dog cat cat fish")), false);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::word_pattern(String::from("aaaa"), String::from("dog cat cat dog")), false);
	}

	#[test]
	fn user1() {
		assert_eq!(Solution::word_pattern(String::from("abba"), String::from("dog cat cat")), false);
	}

	#[test]
	fn user2() {
		assert_eq!(Solution::word_pattern(String::from("ooxx"), String::from("aa aa bb bb bb")), false);
	}
}
