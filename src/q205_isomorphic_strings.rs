pub struct Solution;

impl Solution {
	// 先看每个 t 中字符是否能换为 s 的，再反过来检查是否无重复使用。
	pub fn is_isomorphic(s: String, t: String) -> bool {
		let s = s.as_bytes();
		let t = t.as_bytes();
		if s.len() != t.len() {
			return false;
		}
		return Self::can_map(s, t) && Self::can_map(t, s);
	}

	// 检查 t 的字符是否能替换为 s 的，使其相等。
	fn can_map(s: &[u8], t: &[u8]) -> bool {
		let mut map = [0xFFu8; 128];
		for i in 0..t.len() {
			let p = t[i] as usize;
			let target = map[p];
			if target == 0xFF {
				map[p] = s[i];
			} else if target != s[i] {
				return false;
			}
		}
		return true; // 仅检查单侧替换，还要反过来在查一遍。
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::is_isomorphic(String::from("egg"), String::from("add")), true);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::is_isomorphic(String::from("foo"), String::from("bar")), false);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::is_isomorphic(String::from("paper"), String::from("title")), true);
	}
}
