pub struct Solution {}

impl Solution {
	// 两个指针分别从两侧向内扫描，每次递进更低的那个。
	// 我能想到双指针，但没搞清楚递进条件，浪费了不少时间。
	pub fn max_area(height: Vec<i32>) -> i32 {
		let mut left = 0;
		let mut right = height.len() - 1;
		let mut max_area = 0;

		while left < right {
			let i = height[left];
			let j = height[right];

			let width = (right - left) as i32;
			let area = i.min(j) * width;
			max_area = max_area.max(area);

			if i < j {
				left += 1;
			} else {
				right -= 1;
			}
		}
		return max_area;
	}

	// 暴力搜，N^2 时间复杂度，超时了。
	pub fn max_area_2(height: Vec<i32>) -> i32 {
		let mut area = 0;

		for i in 0..height.len() {
			let h = height[i];
			for j in 0..i {
				let s = height[j];
				area = area.max((s.min(h) as usize) * (i - j));
			}
			for j in i..height.len() {
				let s = height[j];
				area = area.max((s.min(h) as usize) * (j - i));
			}
		}
		return area as i32;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::max_area(vec![1, 8, 6, 2, 5, 4, 8, 3, 7]), 49);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::max_area(vec![1, 1]), 1);
	}
}
