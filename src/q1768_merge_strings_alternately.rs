pub struct Solution {}

// 这题跟 21. Merge Two Sorted Lists 不是一回事吗，还更简单些。
impl Solution {
	pub fn merge_alternately(word1: String, word2: String) -> String {
		let a = word1.as_bytes();
		let b = word2.as_bytes();
		let mut result = Vec::with_capacity(a.len() + b.len());

		let common = a.len().min(b.len());
		for i in 0..common {
			result.push(a[i]);
			result.push(b[i]);
		}

		if a.len() > b.len() {
			result.extend_from_slice(&a[common..]);
		} else {
			result.extend_from_slice(&b[common..]);
		}

		// SAFITY: word1 and word2 consist of lowercase English letters.
		return unsafe { String::from_utf8_unchecked(result) };
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::merge_alternately(String::from("abc"), String::from("pqr")), String::from("apbqcr"));
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::merge_alternately(String::from("ab"), String::from("pqrs")), String::from("apbqrs"));
	}
	#[test]
	fn example3() {
		assert_eq!(Solution::merge_alternately(String::from("abcd"), String::from("pq")), String::from("apbqcd"));
	}
}
