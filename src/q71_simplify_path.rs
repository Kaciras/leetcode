pub struct Solution;

impl Solution {
	// 从后往前按照 .. 的数量跳过父级，另一种做法是使用栈结构。
	pub fn simplify_path(path: String) -> String {
		let mut components = Vec::new();
		let mut parents = 0;
		for c in path.split('/').rev() {
			if c == ".." {
				parents += 1;
			} else if c != "" && c != "." {
				if parents != 0 {
					parents -= 1;
				} else {
					components.push(c);
				}
			}
		}
		components.reverse();
		return format!("/{}", components.join("/"));
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::simplify_path("/home/".into()), "/home");
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::simplify_path("/home//foo/".into()), "/home/foo");
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::simplify_path("/home/user/Documents/../Pictures".into()), "/home/user/Pictures");
	}

	#[test]
	fn example4() {
		assert_eq!(Solution::simplify_path("/../".into()), "/");
	}

	#[test]
	fn example5() {
		assert_eq!(Solution::simplify_path("/.../a/../b/c/../d/./".into()), "/.../b/d");
	}
}
