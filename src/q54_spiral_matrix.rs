pub struct Solution;

impl Solution {
	pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
		let mut solution = SpiralWalker {
			top: 0,
			left: 0,
			right: matrix[0].len(),
			bottom: matrix.len(),
			matrix,
			flatten_values: Vec::new(),
		};
		solution.walk1();
		return solution.flatten_values;
	}
}

pub struct SpiralWalker {
	matrix: Vec<Vec<i32>>,
	flatten_values: Vec<i32>,
	top: usize,
	left: usize,
	right: usize,
	bottom: usize,
}

// 注意 usize 没有负数，不能靠 -1 来判断结束，所以必须右开区间，循环时先减。
impl SpiralWalker {
	fn walk1(&mut self) {
		for i in self.left..self.right {
			self.flatten_values.push(self.matrix[self.top][i]);
		}
		self.top += 1;
		if self.top != self.bottom { self.walk2(); }
	}

	fn walk2(&mut self) {
		self.right -= 1;
		for i in self.top..self.bottom {
			self.flatten_values.push(self.matrix[i][self.right]);
		}
		if self.left != self.right {
			self.walk3();
		}
	}

	fn walk3(&mut self) {
		self.bottom -= 1;
		for i in (self.left..self.right).rev() {
			self.flatten_values.push(self.matrix[self.bottom][i]);
		}
		if self.top != self.bottom {
			self.walk4();
		}
	}

	fn walk4(&mut self) {
		for i in (self.top..self.bottom).rev() {
			self.flatten_values.push(self.matrix[i][self.left]);
		}
		self.left += 1;
		if self.left != self.right { self.walk1(); }
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn case1() {
		let matrix = vec![vec![3], vec![2]];
		assert_eq!(Solution::spiral_order(matrix), vec![3, 2]);
	}

	#[test]
	fn example1() {
		let matrix = vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]];
		assert_eq!(Solution::spiral_order(matrix), vec![1, 2, 3, 6, 9, 8, 7, 4, 5]);
	}

	#[test]
	fn example2() {
		let matrix = vec![vec![1, 2, 3, 4], vec![5, 6, 7, 8], vec![9, 10, 11, 12]];
		assert_eq!(Solution::spiral_order(matrix), vec![1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]);
	}

	#[test]
	fn user1() {
		let matrix = vec![vec![8964]];
		assert_eq!(Solution::spiral_order(matrix), vec![8964]);
	}
}
