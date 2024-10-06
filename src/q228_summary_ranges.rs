pub struct Solution {}

impl Solution {
	// 不好看，如果模拟前探的话也许简单点。
	pub fn summary_ranges(nums: Vec<i32>) -> Vec<String> {
		let mut result = Vec::new();
		if nums.is_empty() {
			return result;
		}
		let mut interval = String::new();
		let mut start = nums[0];
		interval.push_str(nums[0].to_string().as_str());

		for i in 1..nums.len() {
			if nums[i] == nums[i - 1] + 1 {
				continue;
			}
			if nums[i - 1] != start {
				interval.push_str("->");
				interval.push_str(nums[i - 1].to_string().as_str());
			}
			result.push(interval);
			interval = String::new();
			start = nums[i];
			interval.push_str(start.to_string().as_str());
		}
		if nums[nums.len() - 1] != start {
			interval.push_str("->");
			interval.push_str(nums[nums.len() - 1].to_string().as_str());
		}
		result.push(interval);
		return result;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		let ranges = Solution::summary_ranges(vec![0, 1, 2, 4, 5, 7]);
		assert_eq!(ranges, vec!["0->2", "4->5", "7"]);
	}

	#[test]
	fn example2() {
		let ranges = Solution::summary_ranges(vec![0, 2, 3, 4, 6, 8, 9]);
		assert_eq!(ranges, vec!["0", "2->4", "6", "8->9"]);
	}

	#[test]
	fn test1() {
		assert_eq!(Solution::summary_ranges(vec![]), Vec::<String>::new());
	}

	#[test]
	fn test2() {
		assert_eq!(Solution::summary_ranges(vec![1]), vec!["1"]);
	}

	#[test]
	fn test3() {
		assert_eq!(Solution::summary_ranges(vec![1, 2]), vec!["1->2"]);
	}
}
