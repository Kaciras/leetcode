pub struct Solution;

impl Solution {
	pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
		let s = s.as_bytes();

		let mut dp = vec![false; s.len() + 1];
		dp[0] = true;

		for i in 0..dp.len() {
			if !dp[i] {
				continue;
			}
			for p in word_dict.iter() {
				if s[i..].starts_with(p.as_bytes()) {
					dp[i + p.len()] = true;
				}
			}
		}
		return dp[s.len()];
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	fn invoke(s: &str, dict: &[&str]) -> bool {
		let dict = dict.into_iter().map(|&x| String::from(x)).collect();
		return Solution::word_break(s.into(), dict);
	}

	#[test]
	fn example1() {
		assert!(invoke("leetcode", &["leet", "code"]));
	}

	#[test]
	fn example2() {
		assert!(invoke("applepenapple", &["apple", "pen"]));
	}

	#[test]
	fn example3() {
		assert!(!invoke("catsandog", &["cats", "dog", "sand", "and", "cat"]));
	}
}
