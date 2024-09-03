pub struct Solution {}

// 这个傻屄题目给的描述里不包括嵌套的情况，但测试用例里有。
impl Solution {
	pub fn longest_valid_parentheses(s: String) -> i32 {
		let mut left = 0;
		let mut right = 0;
		let mut max = 0;

		for ch in s.chars() {
			if ch == '(' {
				left += 1;
			} else {
				right += 1;
			}
			if left == right {
				max = max.max(left + right);
			} else if left < right {
				(left, right) = (0, 0);
			}
		}

		(left, right) = (0, 0);

		for ch in s.chars().rev() {
			if ch == '(' {
				left += 1;
			} else {
				right += 1;
			}
			if left == right {
				max = max.max(left + right);
			} else if left > right {
				(left, right) = (0, 0);
			}
		}

		return max;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::longest_valid_parentheses("(()".into()), 2);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::longest_valid_parentheses(")()())".into()), 4);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::longest_valid_parentheses("".into()), 0);
	}

	#[test]
	fn test1() {
		assert_eq!(Solution::longest_valid_parentheses("(".into()), 0);
	}

	#[test]
	fn test2() {
		assert_eq!(Solution::longest_valid_parentheses("()(".into()), 2);
	}

	#[test]
	fn test3() {
		assert_eq!(Solution::longest_valid_parentheses("()(())".into()), 6);
	}

	#[test]
	fn test4() {
		assert_eq!(Solution::longest_valid_parentheses("()(()".into()), 2);
	}
}
