pub struct Solution {}

// 没啥好说的，删除时直接把末尾的换过来即可。
impl Solution {
	pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
		let mut k = nums.len();
		let mut i = 0;
		while i < k {
			if nums[i] == val {
				k -= 1;
				nums[i] = nums[k];
			} else {
				i += 1;
			}
		}
		return k as i32;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		let mut array = vec![3, 2, 2, 3];
		let size = Solution::remove_element(&mut array, 3);
		assert_eq!(size, 2);
		assert_eq!(array[0..size as usize], vec![2, 2]);
	}

	#[test]
	fn example2() {
		let mut array = vec![0,1,2,2,3,0,4,2];
		let size = Solution::remove_element(&mut array, 2);
		assert_eq!(size, 5);
		assert_eq!(array[0..size as usize], vec![0,1,4,0,3]);
	}

}
