pub struct Solution {}

impl Solution {
	pub fn cal_points(operations: Vec<String>) -> i32 {
		let mut stack = Vec::new();
		for operation in operations {
			match operation.as_str() {
				"+" => {
					let a = stack[stack.len() - 1];
					let b = stack[stack.len() - 2];
					stack.push(a + b);
				}
				"C" => {
					stack.pop();
				}
				"D" => {
					let a = stack.last().unwrap();
					stack.push(a * 2)
				}
				// parse 可以代替 i32::from_str_radix
				x => stack.push(x.parse().unwrap()),
			}
		}
		return stack.iter().sum();
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	fn invoke(input: &[&str]) -> i32 {
		return Solution::cal_points(input.into_iter().map(|&x| String::from(x)).collect());
	}

	#[test]
	fn example1() {
		assert_eq!(invoke(&["5", "2", "C", "D", "+"]), 30);
	}

	#[test]
	fn example2() {
		assert_eq!(invoke(&["5", "-2", "4", "C", "D", "9", "+", "+"]), 27);
	}

	#[test]
	fn example3() {
		assert_eq!(invoke(&["1", "C"]), 0);
	}
}
