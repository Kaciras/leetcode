use std::cmp::Ordering;

pub struct Solution {}

impl Solution {
	pub fn insert(mut intervals: Vec<Vec<i32>>, target: Vec<i32>) -> Vec<Vec<i32>> {
		let found = intervals.binary_search_by(|x| {
			if target[0] > x[1] {
				Ordering::Less
			} else if target[1] < x[0] {
				Ordering::Greater
			} else {
				Ordering::Equal
			}
		});
		if let Err(i) = found {
			intervals.insert(i, target);
		} else {
			let i = found.unwrap();
			let mut k = i;
			while k > 0 && intervals[k - 1][1] >= target[0] {
				k -= 1
			}
			let mut e = i;
			while e < intervals.len() - 1 && intervals[e + 1][0] < target[1] {
				e += 1;
			}
			let merged = vec![
				intervals[k][0].min(target[0]),
				intervals[e][1].max(target[1])
			];
			intervals[k] = merged;
			intervals.drain(k + 1..e + 1);
		}
		return intervals;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		let mut input = vec![vec![1, 3], vec![6, 9]];
		assert_eq!(Solution::insert(input, vec![2, 5]), vec![vec![1, 5], vec![6, 9]]);
	}

	#[test]
	fn example2() {
		let mut input = vec![vec![1, 2], vec![3, 5], vec![6, 7], vec![8, 10], vec![12, 16]];
		assert_eq!(Solution::insert(input, vec![4, 8]), vec![vec![1, 2], vec![3, 10], vec![12, 16]]);
	}

	#[test]
	fn test1() {
		let mut input = vec![];
		assert_eq!(Solution::insert(input, vec![1, 2]), vec![vec![1, 2]]);
	}

	#[test]
	fn test2() {
		let mut input = vec![vec![1, 2], vec![4, 5]];
		assert_eq!(Solution::insert(input, vec![7, 8]), vec![vec![1, 2], vec![4, 5], vec![7, 8]]);
	}

	#[test]
	fn test3() {
		let mut input = vec![vec![1, 2], vec![4, 5]];
		assert_eq!(Solution::insert(input, vec![0, 6]), vec![vec![0, 6]]);
	}
}
