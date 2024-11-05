pub struct Solution;

impl Solution {
	pub fn can_complete_circuit(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
		// 仅当一圈之后剩余油为负数时才跑不完全程。
		let mut remain = 0;
		let mut tank = 0;
		let mut start = 0;

		for i in 0..gas.len() {
			let diff = gas[i] - cost[i];
			remain += diff;
			tank += diff;

			// 若从 0 开到某处后跑不到下一个，那么从之间的位置开始也不可能。
			if tank < 0 {
				tank = 0;
				start = i + 1;
			}
		}
		return if remain < 0 { -1 } else { start as i32 };
	}

	// 模拟整个过程，O(n^2) 超时了。
	pub fn can_complete_circuit_1(gas: Vec<i32>, cost: Vec<i32>) -> i32 {
		for i in 0..gas.len() {
			let mut tank = 0;
			let mut pass = true;
			for j in 0..gas.len() {
				let k = (i + j) % gas.len();
				tank += gas[k];
				tank -= cost[k];
				if tank < 0 {
					pass = false;
					break;
				}
			}
			if pass {
				return i as i32;
			}
		}
		return -1;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::can_complete_circuit(vec![1, 2, 3, 4, 5], vec![3, 4, 5, 1, 2]), 3);
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::can_complete_circuit(vec![2, 3, 4], vec![3, 4, 3]), -1);
	}

	#[test]
	fn case1() {
		assert_eq!(Solution::can_complete_circuit(vec![3, 1, 1], vec![1, 2, 2]), 0);
	}

	#[test]
	fn user1() {
		let mut cost = vec![0; 1e6 as usize];
		let mut gas = vec![0; 1e6 as usize];
		gas[90001] = 2;
		cost[90000] = 1;
		assert_eq!(Solution::can_complete_circuit(gas, cost), 90001);
	}
}
