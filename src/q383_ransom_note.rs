pub struct Solution;

impl Solution {
	pub fn can_construct(ransom_note: String, magazine: String) -> bool {
		if ransom_note.len() > magazine.len() {
			return false;
		}
		let mut counter = [0; 26];
		for c in magazine.bytes() {
			counter[(c - b'a') as usize] += 1;
		}
		return ransom_note.bytes().all(|c| {
			let i = (c - b'a') as usize;
			let count = &mut counter[i];
			*count -= 1;
			return *count != -1; // 减超了表明字母不够用了。
		});
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::can_construct(String::from("a"), String::from("b")), false);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::can_construct(String::from("aa"), String::from("ab")), false);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::can_construct(String::from("aa"), String::from("aab")), true);
	}
}
