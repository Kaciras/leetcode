pub struct Solution;

impl Solution {
	pub fn min_path_sum(mut grid: Vec<Vec<i32>>) -> i32 {
		// 第一行和第一列没有之前的，特殊处理，当然放到循环里 if 也行。
		for i in 1..grid[0].len() {
			grid[0][i] += grid[0][i - 1];
		}
		for i in 1..grid.len() {
			grid[i][0] += grid[i - 1][0];
		}
		for i in 1..grid.len() {
			for j in 1..grid[i].len() {
				grid[i][j] += grid[i][j - 1].min(grid[i - 1][j]);
			}
		}
		return grid[grid.len() - 1][grid[0].len() - 1];
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::min_path_sum(vec![vec![1, 3, 1], vec![1, 5, 1], vec![4, 2, 1]]), 7);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::min_path_sum(vec![vec![1, 2, 3], vec![4, 5, 6]]), 12);
	}
}

