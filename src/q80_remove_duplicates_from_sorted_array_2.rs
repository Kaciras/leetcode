pub struct Solution {}

impl Solution {
	pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
		let mut previous = nums[0];
		let mut repeat = 1;
		let mut removes = 0;

		for i in 1..nums.len() {
			if previous == nums[i] {
				repeat += 1;
			} else {
				repeat = 1;
				previous = nums[i]
			}
			if repeat > 2 {
				removes += 1;
				nums[i] = i32::MAX;
			}
		}
		// Rust 当前的实现是快排，不需要空间，倒也符合题目条件……
		nums.sort_unstable();
		return (nums.len() - removes) as i32;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		let mut array = vec![1, 1, 1, 2, 2, 3];
		let size = Solution::remove_duplicates(&mut array);
		assert_eq!(size, 5);
		assert_eq!(array[0..size as usize], vec![1, 1, 2, 2, 3]);
	}

	#[test]
	fn example2() {
		let mut array = vec![0, 0, 1, 1, 1, 1, 2, 3, 3];
		let size = Solution::remove_duplicates(&mut array);
		assert_eq!(size, 7);
		assert_eq!(array[0..size as usize], vec![0, 0, 1, 1, 2, 3, 3]);
	}

	#[test]
	fn test1() {
		let mut array = vec![0];
		let size = Solution::remove_duplicates(&mut array);
		assert_eq!(size, 1);
		assert_eq!(array[0..size as usize], vec![0]);
	}
}
