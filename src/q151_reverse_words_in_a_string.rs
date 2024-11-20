pub struct Solution;

fn index_of<T: Fn(&u8) -> bool>(array: &[u8], start: usize, predicate: T) -> Option<usize> {
	return array.iter().skip(start).position(predicate).map(|i| i + start);
}

// 分组翻转一般都能用两次翻转法来处理。
impl Solution {
	pub fn reverse_words(mut s: String) -> String {
		// SAFITY: s contains English letters, digits, and spaces
		let chars = unsafe { s.as_bytes_mut() };
		chars.reverse();

		let mut src_index = 0;
		let mut dest_index = 0;

		while src_index < chars.len() {
			let b = index_of(chars, src_index, |&b| b != b' ');
			if b.is_none() {
				break; // 扫完了
			}
			let b = b.unwrap();
			let e = index_of(chars, b, |&b| b == b' ').unwrap_or(chars.len());

			let mut word = &mut chars[b..e];
			word.reverse();

			if dest_index != 0 {
				chars[dest_index] = b' ';
				dest_index += 1;
			}
			chars.copy_within(b..e, dest_index);
			(src_index, dest_index) = (e, dest_index + e - b);
		}

		s.truncate(dest_index);
		return s;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn case1() {
		assert_eq!(Solution::reverse_words(String::from("EPY2giL")), String::from("EPY2giL"));
	}

	#[test]
	fn example1() {
		assert_eq!(Solution::reverse_words(String::from("the sky is blue")), String::from("blue is sky the"));
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::reverse_words(String::from("  hello world  ")), String::from("world hello"));
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::reverse_words(String::from("a good   example")), String::from("example good a"));
	}
}
