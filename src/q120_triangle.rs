pub struct Solution;

// 最基础的 DP 题，没什么好说的，一次就搞定了。
impl Solution {
	pub fn minimum_total(mut triangle: Vec<Vec<i32>>) -> i32 {
		let final_level = Self::dp(triangle);
		return *final_level.iter().min().unwrap();
	}

	fn dp(mut triangle: Vec<Vec<i32>>) -> Vec<i32> {
		let mut v = triangle.pop().unwrap();
		if v.len() == 1 {
			return v;
		}
		let previous = Self::dp(triangle);
		let end = v.len() - 1;

		v[0] += previous[0];
		v[end] += previous[end - 1];
		for i in 1..end {
			v[i] += previous[i].min(previous[i - 1]);
		}

		return v; // 每个格子的累计路径是上面两个中小的加自身的值。
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		let t = vec![vec![2], vec![3, 4], vec![6, 5, 7], vec![4, 1, 8, 3]];
		assert_eq!(Solution::minimum_total(t), 11);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::minimum_total(vec![vec![-10]]), -10);
	}
}
