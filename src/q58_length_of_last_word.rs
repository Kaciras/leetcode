pub struct Solution;

// 原来 u8 可以直接写成 b + 字符，不需要去一个个查 ASCII 了。
impl Solution {
	pub fn length_of_last_word(s: String) -> i32 {
		let s = s.as_bytes();
		let e = s.iter().rposition(|&x| x != b' ').unwrap();
		let b = s[0..e].iter().rposition(|&x| x == b' ');
		return match b {
			None => { e as i32 + 1 }
			Some(x) => { (e - x) as i32 }
		};
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::length_of_last_word(String::from("Hello World")), 5);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::length_of_last_word(String::from("   fly me   to   the moon  ")), 4);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::length_of_last_word(String::from("luffy is still joyboy")), 6);
	}

	#[test]
	fn case1() {
		assert_eq!(Solution::length_of_last_word(String::from("a")), 1);
	}
}
