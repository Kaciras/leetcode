pub struct Solution {}

// 跟计数排序类似的思想，统计每种被引用数出现的次数，然后从大到小找超过该引用数的位置。
impl Solution {
	pub fn h_index(citations: Vec<i32>) -> i32 {
		// 被引用 k 次的有 v 篇
		let mut count = [0; 1001];
		for c in citations {
			count[c as usize] += 1;
		}
		let mut sum = 0;
		for i in (0..1001).rev() {
			sum += count[i];
			if sum >= i {
				return i as i32;
			}
		}
		panic!("Always return in above loop");
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::h_index(vec![3, 0, 6, 1, 5]), 3);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::h_index(vec![1, 3, 1]), 1);
	}
}
