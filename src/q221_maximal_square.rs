pub struct Solution;

// 我想到了看三个相邻的格子，但细节还想不出来，不知道是刷少了还是怎得。
// https://leetcode.com/problems/maximal-square/solutions/600149/python-thinking-process-diagrams-dp-approach/?envType=study-plan-v2&envId=top-interview-150
impl Solution {
	pub fn maximal_square(matrix: Vec<Vec<char>>) -> i32 {
		let mut dp = vec![
			vec![0; matrix[0].len() + 1]; matrix.len() + 1
		];
		let mut max_side = 0;
		for i in 0..matrix.len() {
			for j in 0..matrix[0].len() {
				if matrix[i][j] == '1' {
					dp[i + 1][j + 1] = 1 + dp[i][j]
						.min(dp[i][j + 1])
						.min(dp[i + 1][j]);
					max_side = max_side.max(dp[i + 1][j + 1]);
				}
			}
		}
		return max_side * max_side;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		let matrix = vec![
			vec!['1', '0', '1', '0', '0'],
			vec!['1', '0', '1', '1', '1'],
			vec!['1', '1', '1', '1', '1'],
			vec!['1', '0', '0', '1', '0'],
		];
		assert_eq!(Solution::maximal_square(matrix), 4);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::maximal_square(vec![vec!['0', '1'], vec!['1', '0', ]]), 1);
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::maximal_square(vec![vec!['0']]), 0);
	}
}
