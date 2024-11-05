pub struct Solution;

impl Solution {
	pub fn h_index(citations: Vec<i32>) -> i32 {
		let mut lo = 0usize;
		let mut hi = citations.len();
		let mut max = 0;

		while lo < hi {
			let mid = lo + (hi - lo) / 2;
			let count = citations.len() - mid;
			let cited = citations[mid] as usize;

			if cited >= count {
				hi = mid;
				max = max.max(count);
			} else {
				lo = mid + 1;
			}
		}
		return max as i32;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn case1() {
		assert_eq!(Solution::h_index(vec![0]), 0);
	}

	#[test]
	fn case2() {
		assert_eq!(Solution::h_index(vec![100]), 1);
	}

	#[test]
	fn case3() {
		assert_eq!(Solution::h_index(vec![11, 15]), 2);
	}

	#[test]
	fn example1() {
		assert_eq!(Solution::h_index(vec![0, 1, 3, 5, 6]), 3);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::h_index(vec![1, 2, 100]), 2);
	}
}
