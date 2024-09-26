pub struct Solution {}

const L_BRACKET: u8 = 40;
const R_BRACKET: u8 = 41;
const ADD: u8 = 43;
const MINUS: u8 = 45;
const ZERO: u8 = 48;
const NINE: u8 = 58;

impl Solution {
	pub fn calculate(s: String) -> i32 {
		let mut stack = vec![1];
		let mut result = 0;
		let mut num = 0;
		let mut sign = 1i32;
		let mut scope = 1i32;

		for c in s.as_bytes() {
			let c = *c;

			if c >= ZERO && c <= NINE {
				num = num * 10 + ((c as i32) - 48);
				continue;
			}

			result += scope * num * sign;
			num = 0;

			match c {
				MINUS => sign = -1,
				ADD => sign = 1,
				L_BRACKET => {
					stack.push(sign);
					if sign == -1 {
						scope = -scope;
					}
					sign = 1;
				}
				R_BRACKET => {
					if stack.pop() == Some(-1) {
						scope = -scope;
					}
				}
				_ => { /* space */ }
			}
		}
		return result + scope * num * sign;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::calculate(String::from("1 + 1")), 2);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::calculate(String::from(" 2-1 + 2 ")), 3);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::calculate(String::from("(1+(4+5+2)-3)+(6+8)")), 23);
	}

	#[test]
	fn case1() {
		assert_eq!(Solution::calculate(String::from("(7)-(0)+(4)")), 11);
	}

	// 题目不是说减号一定是运算而不是负号么……
	#[test]
	fn case2() {
		assert_eq!(Solution::calculate(String::from("- (3 + (4 + 5))")), -12);
	}

	#[test]
	fn test1() {
		assert_eq!(Solution::calculate(String::from("(123 + 5)")), 128);
	}

	#[test]
	fn test2() {
		assert_eq!(Solution::calculate(String::from("9-(2-(1-1))")), 7);
	}
}
