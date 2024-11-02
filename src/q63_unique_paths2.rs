pub struct Solution;

// 很简单的题，思路就是上面的 + 左边的路径数，遇到大石头把路径数量设为 0.
impl Solution {
	pub fn unique_paths_with_obstacles(mut grid: Vec<Vec<i32>>) -> i32 {
		for i in 0..grid.len() {
			for j in 0..grid[i].len() {
				let down = if i == 0 { 0 } else { grid[i - 1][j] };
				let right = if j == 0 { 0 } else { grid[i][j - 1] };

				if grid[i][j] == 1 {
					grid[i][j] = 0;
				} else if i == 0 && j == 0 {
					grid[i][j] = 1;
				} else {
					grid[i][j] = down + right;
				}
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
		assert_eq!(Solution::unique_paths_with_obstacles(vec![vec![0, 0, 0], vec![0, 1, 0], vec![0, 0, 0]]), 2);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::unique_paths_with_obstacles(vec![vec![0, 1], vec![0, 0]]), 1);
	}
}
