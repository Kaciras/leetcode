pub struct Solution {}

// 类似 3sum 中的两侧逼近法，这类问题几乎都可以用这种方案。
impl Solution {
	pub fn three_sum_closest(mut nums: Vec<i32>, target: i32) -> i32 {
		nums.sort_unstable();

		let mut closest = i32::MAX;
		let mut min_diff = closest;

		// 外层遍历每个数，因为俩指针都在后面所以倒数第二个即结束。
		for i in 0..nums.len() - 2 {
			let mut left = i + 1;
			let mut right = nums.len() - 1;
			while left < right {
				let sum = nums[i] + nums[left] + nums[right];

				// 如果小了就增加一下左侧，反之亦然。
				if sum < target {
					left += 1;
				} else if sum > target {
					right -= 1;
				} else {
					// 运气好找到相等的，可以直接结束。
					return sum;
				}

				// 不相等的话就更新下最近似的值。
				let diff = (target - sum).abs();
				if diff < min_diff {
					closest = sum;
					min_diff = diff;
				}
			}
		}
		return closest;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::three_sum_closest(vec![-1, 2, 1, -4], 1), 2);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::three_sum_closest(vec![0, 0, 0], 1), 0);
	}
}
