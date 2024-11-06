pub struct Solution;

impl Solution {
	pub fn num_decodings(s: String) -> i32 {
		let s = s.as_bytes();
		let mut dp = vec![0; s.len() + 1];

		if s[0] == b'0' {
			return 0;
		};

		dp[0] = 1;
		dp[1] = 1;

		for (i, &c) in s.iter().enumerate().skip(1) {
			let p = s[i - 1];
			if c != b'0' {
				dp[i + 1] = dp[i];
			}
			if p == b'1' || p == b'2' && c <= b'6' {
				dp[i + 1] += dp[i - 1];
			}
		}
		return dp[s.len()];
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::num_decodings("12".into()), 2);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::num_decodings("226".into()), 3);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::num_decodings("06".into()), 0);
	}

	#[test]
	fn test1() {
		assert_eq!(Solution::num_decodings("30".into()), 0);
	}

	#[test]
	fn test2() {
		assert_eq!(Solution::num_decodings("27".into()), 1);
	}
}
