pub struct Solution;

impl Solution {
	// 每列能接的水等于两侧最高值中较小的，减去该列的高度，最高值可以提前计算。
	pub fn trap(height: Vec<i32>) -> i32 {
		let last_index = height.len() - 1;
		if last_index < 2 {
			return 0;
		}
		let mut lmax = vec![0; height.len()];
		let mut rmax = vec![0; height.len()];
		lmax[0] = height[0];
		rmax[last_index] = height[last_index];

		for i in 1..height.len() {
			lmax[i] = lmax[i - 1].max(height[i]);
		}
		for i in (0..height.len() - 1).rev() {
			rmax[i] = rmax[i + 1].max(height[i]);
		}
		return (0..height.len())
			.fold(0, |w, i| w + lmax[i].min(rmax[i]) - height[i]);
	}

	// 分层计数法，从上到下每层找左右边界，然后统计中间空洞的数量，最后加起来。
	pub fn trap_1(height: Vec<i32>) -> i32 {
		let top = *height.iter().max().unwrap();
		let height = height.as_slice();
		return (0..=top)
			.rev()
			.map(|i| Self::count_layer(height, i)).sum();
	}

	fn count_layer(height: &[i32], level: i32) -> i32 {
		let s = height.iter().position(|&h| h >= level).unwrap();
		let e = height.iter().rposition(|&h| h >= level).unwrap();
		height[s..e].iter().filter(|&&h| h < level).count() as i32
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::trap(vec![0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::trap(vec![4, 2, 0, 3, 2, 5]), 9);
	}
}
