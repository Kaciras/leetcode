pub struct Solution;

const T4: [&'static str; 10] = ["", "M", "MM", "MMM", "", "", "", "", "", ""];
const T3: [&'static str; 10] = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"];
const T2: [&'static str; 10] = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"];
const T1: [&'static str; 10] = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"];

// 我这查表法竟然不是第一快？看来 LeetCode 的服务器得升级了。
impl Solution {

	// num < 4000，最长也就 15 个字符（3888 = MMMDCCCLXXXVIII）
	pub fn int_to_roman(n: i32) -> String {
		let n = n as usize;
		return [T4[n / 1000], T3[n / 100 % 10], T2[n / 10 % 10], T1[n % 10]].join("");
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::int_to_roman(3000), "MMM");
		assert_eq!(Solution::int_to_roman(700), "DCC");
		assert_eq!(Solution::int_to_roman(40), "XL");
		assert_eq!(Solution::int_to_roman(9), "IX");
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::int_to_roman(58), "LVIII");
	}

	#[test]
	fn example3() {
		assert_eq!(Solution::int_to_roman(1994), "MCMXCIV");
	}

	#[test]
	fn test1() {
		assert_eq!(Solution::int_to_roman(3888), "MMMDCCCLXXXVIII");
	}
}
