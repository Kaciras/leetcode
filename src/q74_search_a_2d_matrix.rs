use std::ops::Index;

pub struct Solution {}

struct MatrixVec2D {
	matrix: Vec<Vec<i32>>,
}

impl MatrixVec2D {
	fn len(&self) -> usize {
		self.matrix.len() * self.matrix[0].len()
	}
}

impl Index<usize> for MatrixVec2D {
	type Output = i32;

	fn index(&self, index: usize) -> &Self::Output {
		let i = index / self.matrix[0].len();
		let j = index % self.matrix[0].len();
		return &self.matrix[i][j];
	}
}

impl Solution {
	// 先二分第一列确定行，再二分该行确定值。
	pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
		match matrix.binary_search_by(|row| row[0].cmp(&target)) {
			Ok(row_idx) => true,
			Err(row_idx) => {
				if row_idx == 0 {
					false
				} else {
					matrix[row_idx - 1][1..].binary_search(&target).is_ok()
				}
			}
		}
	}

	// 直接适配矩阵为展平的列表。
	pub fn search_matrix_1(matrix: Vec<Vec<i32>>, target: i32) -> bool {
		let vec = MatrixVec2D { matrix };
		let mut lo = 0;
		let mut hi = vec.len();

		while lo < hi {
			let mid = lo + (hi - lo) / 2;
			if vec[mid] == target {
				return true;
			} else if vec[mid] > target {
				hi = mid;
			} else {
				lo = mid + 1;
			}
		}
		return false;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn case1() {
		let martix = vec![vec![1], vec![1]];
		assert_eq!(Solution::search_matrix(martix, 0), false);
	}

	#[test]
	fn case2() {
		let martix = vec![vec![1, 1]];
		assert_eq!(Solution::search_matrix(martix, 0), false);
	}

	#[test]
	fn example1() {
		let martix = vec![
			vec![1, 3, 5, 7],
			vec![10, 11, 16, 20],
			vec![23, 30, 34, 60]
		];
		assert_eq!(Solution::search_matrix(martix, 3), true);
	}

	#[test]
	fn example2() {
		let martix = vec![
			vec![1, 3, 5, 7],
			vec![10, 11, 16, 20],
			vec![23, 30, 34, 60]
		];
		assert_eq!(Solution::search_matrix(martix, 13), false);
	}

	#[test]
	fn user1() {
		let martix = vec![vec![114514]];
		assert_eq!(Solution::search_matrix(martix, 24), false);
	}
}
