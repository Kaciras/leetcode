use rand::prelude::SliceRandom;
use std::collections::HashMap;

struct Solution {
	indecies: HashMap<i32, Vec<i32>>,
}

impl Solution {
	fn new(nums: Vec<i32>) -> Self {
		let mut indecies = HashMap::new();
		for i in 0..nums.len() {
			indecies
				.entry(nums[i])
				.or_insert_with(Vec::new)
				.push(i as i32);
		}
		return Self { indecies };
	}

	fn pick(&self, target: i32) -> i32 {
		let values = self.indecies.get(&target).unwrap();
		return *values.choose(&mut rand::thread_rng()).unwrap();
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		let sln = Solution::new(vec![1, 2, 3, 3, 3]);
		println!("{:?}", sln.pick(3));
		println!("{:?}", sln.pick(1));
		println!("{:?}", sln.pick(3));
	}
}
