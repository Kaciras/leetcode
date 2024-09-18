
pub struct Solution {}

impl Solution {

	// 依赖了外部的 API，不好自己写测试。
	#![allow(non_snake_case)]
	fn isBadVersion(&self, _: i32) -> bool {
		return false;
	}

	pub fn first_bad_version(&self, n: i32) -> i32 {
		let mut s = 0;
		let mut e = n;

		while e > s {
			let mid = s + ((e - s) >> 1);
			if self.isBadVersion(mid) {
				e = mid;
			} else {
				s = mid + 1;
			}
		}
		return s; // 二分题好他妈多啊，果然刷题就是无聊。
	}
}
