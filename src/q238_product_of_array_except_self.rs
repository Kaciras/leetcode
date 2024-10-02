pub struct Solution {}

// 不让用除法的话就分成前后缀积相乘。
impl Solution {
	pub fn product_except_self(mut nums: Vec<i32>) -> Vec<i32> {
		let e = nums.len() - 1;
		let mut result = nums.clone();
		for i in 1..nums.len() {
			nums[i] *= nums[i - 1];
		}
		for i in (0..e).rev() {
			result[i] *= result[i + 1];
		}
		result[0] = result[1];
		for i in (1..e) {
			result[i] = nums[i - 1] * result[i + 1];
		}
		result[e] = nums[e - 1];
		return result;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::product_except_self(vec![1, 2, 3, 4]), vec![24, 12, 8, 6]);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::product_except_self(vec![-1, 1, 0, -3, 3]), vec![0, 0, 9, 0, 0]);
	}

	#[test]
	fn test1() {
		assert_eq!(Solution::product_except_self(vec![2, 2, 2, 2]), vec![8, 8, 8, 8]);
	}

	#[test]
	fn test2() {
		assert_eq!(Solution::product_except_self(vec![2, 3]), vec![3, 2]);
	}
}
