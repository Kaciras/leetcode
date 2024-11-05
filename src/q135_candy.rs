pub struct Solution;

impl Solution {
	// 正向扫一遍，遇上坡 +1，再反过来一遍，最后每个位置取最大值。
	// 关于上坡下坡的都应当考虑使用两次扫描法。
	pub fn candy(ratings: Vec<i32>) -> i32 {
		let mut candies = vec![1; ratings.len()];
		for i in 1..ratings.len() {
			if ratings[i] > ratings[i - 1] {
				candies[i] = candies[i - 1] + 1;
			}
		}
		for i in (0..ratings.len() - 1).rev() {
			if ratings[i] > ratings[i + 1]
				&& candies[i] <= candies[i + 1]
			{
				candies[i] = candies[i + 1] + 1;
			}
		}
		return candies.iter().sum();
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn case1() {
		assert_eq!(Solution::candy(vec![1, 3, 4, 5, 2]), 11);
	}

	#[test]
	fn example1() {
		assert_eq!(Solution::candy(vec![1, 0, 2]), 5);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::candy(vec![1, 2, 2]), 4);
	}
}
