pub struct Solution {}

// 主要数的数量大于一般，故减去其它的数量一定为正。
impl Solution {
	pub fn majority_element(nums: Vec<i32>) -> i32 {
		let mut result = 0;
		let mut count = 0;

		for v in nums {
			if v == result {
				count += 1;
			} else if count == 0 {
				result = v;
			} else {
				count -= 1;
			}
		}
		return result;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::majority_element(vec![3, 2, 3]), 3);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::majority_element(vec![2, 2, 1, 1, 1, 2, 2]), 2);
	}
}
