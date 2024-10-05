pub struct Solution {}

type Vector2D = (usize, usize);

impl Solution {
	// 这里的思路是从中间搜索，判断是否联通边界，而且使用了额外的空间保存路径。
	// 更好地方案是从边缘开始，并通过临时赋值记录看过的。
	pub fn solve(board: &mut Vec<Vec<char>>) {
		let m = board.len();
		let n = board[0].len();

		let mut seen = vec![vec![false; n]; m];
		let mut points = Vec::with_capacity(m * n);

		// 注意 zip 只迭代对应的索引对，而不是笛卡尔积，Rust 不自带同时遍历俩的函数。
		for i in 1..m - 1 {
			for j in 1..n - 1 {
				if board[i][j] == 'X' {
					continue;
				}
				points.clear();
				if !Self::dfs(board, &mut seen, &mut points, i, j) {
					points.iter().for_each(|&(i, j)| board[i][j] = 'X');
				}
			}
		}
	}

	fn dfs(board: &Vec<Vec<char>>, seen: &mut Vec<Vec<bool>>, points: &mut Vec<Vector2D>, i: usize, j: usize) -> bool {
		if board[i][j] == 'X' {
			return false;
		}
		if seen[i][j] {
			return false;
		}
		seen[i][j] = true;
		points.push((i, j));

		if i == 0 || i == board.len() - 1 || j == 0 || j == board[0].len() - 1 {
			return true;
		}
		return Self::dfs(board, seen, points, i - 1, j)
			| Self::dfs(board, seen, points, i, j - 1)
			| Self::dfs(board, seen, points, i + 1, j)
			| Self::dfs(board, seen, points, i, j + 1);
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn case1() {
		let mut martix = vec![
			vec!['X', 'O', 'X', 'X'],
			vec!['O', 'X', 'O', 'X'],
			vec!['X', 'O', 'X', 'O'],
			vec!['O', 'X', 'O', 'X'],
		];
		let output = vec![
			vec!['X', 'O', 'X', 'X'],
			vec!['O', 'X', 'X', 'X'],
			vec!['X', 'X', 'X', 'O'],
			vec!['O', 'X', 'O', 'X'],
		];
		Solution::solve(&mut martix);
		assert_eq!(martix, output);
	}

	#[test]
	fn example1() {
		let mut martix = vec![
			vec!['X', 'X', 'X', 'X'],
			vec!['X', 'O', 'O', 'X'],
			vec!['X', 'X', 'O', 'X'],
			vec!['X', 'O', 'X', 'X'],
		];
		let output = vec![
			vec!['X', 'X', 'X', 'X'],
			vec!['X', 'X', 'X', 'X'],
			vec!['X', 'X', 'X', 'X'],
			vec!['X', 'O', 'X', 'X'],
		];
		Solution::solve(&mut martix);
		assert_eq!(martix, output);
	}

	#[test]
	fn example2() {
		let mut martix = vec![vec!['X']];
		let output = vec![vec!['X']];
		Solution::solve(&mut martix);
		assert_eq!(martix, output);
	}

	#[test]
	fn test1() {
		let mut martix = vec![
			vec!['X', 'X', 'X', 'X'],
			vec!['X', 'O', 'O', 'X'],
			vec!['X', 'O', 'O', 'X'],
			vec!['X', 'O', 'X', 'X'],
		];
		let output = vec![
			vec!['X', 'X', 'X', 'X'],
			vec!['X', 'O', 'O', 'X'],
			vec!['X', 'O', 'O', 'X'],
			vec!['X', 'O', 'X', 'X'],
		];
		Solution::solve(&mut martix);
		assert_eq!(martix, output);
	}
}
