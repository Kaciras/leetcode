use std::cmp::Ordering;

pub struct Solution;

impl Solution {
	pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
		let mut i = 0;
		let mut j = numbers.len() - 1;
		while i < j {
			match (numbers[i] + numbers[j]).cmp(&target) {
				Ordering::Equal => { break; }
				Ordering::Less => { i += 1; }
				Ordering::Greater => { j -= 1; }
			}
		}
		return vec![i as i32 + 1, j as i32 + 1];
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::two_sum(vec![2, 7, 11, 15], 9), vec![1, 2]);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::two_sum(vec![2, 3, 4], 6), vec![1, 3]);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::two_sum(vec![-1, 0], -1), vec![1, 2]);
	}
}
