pub struct Solution;

// 按位一个个相乘吧，原先想多位（u64::MAX.log10）一组提升性能但太复杂了。
impl Solution {
	pub fn multiply(num1: String, num2: String) -> String {
		// 特殊情况，为 0 的话需要返回 "0" 而不是空串。
		if num1 == "0" || num2 == "0" {
			return "0".to_string();
		}
		let mut num1 = num1.as_bytes();
		let mut num2 = num2.as_bytes();

		// 两数积的位数最多为两数的位数之和。
		let mut result: Vec<u8> = vec![0; num1.len() + num2.len()];

		// 两个位数相乘可能进位，故 i+j+1 是低位，i+j 是高位。
		for i in (0..num1.len()).rev() {
			for j in (0..num2.len()).rev() {
				let m = (num1[i] - b'0') * (num2[j] - b'0');
				let v = result[i + j + 1] + m;
				result[i + j] += v / 10;
				result[i + j + 1] = v % 10;
			}
		}

		// 范围移除为什么叫 drain 这么奇怪的名字？
		let i = result.iter().position(|&x| x != 0).unwrap();
		result.drain(0..i);

		for v in result.iter_mut() {
			*v += b'0';
		}
		return unsafe { String::from_utf8_unchecked(result) };
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		assert_eq!(Solution::multiply(String::from("2"), String::from("3")), String::from("6"));
	}

	#[test]
	fn example2() {
		assert_eq!(Solution::multiply(String::from("123"), String::from("456")), String::from("56088"));
	}

	#[test]
	fn user1() {
		assert_eq!(Solution::multiply(String::from("0"), String::from("0")), String::from("0"));
	}

	#[test]
	fn user2() {
		assert_eq!(Solution::multiply(String::from("99"), String::from("0")), String::from("0"));
	}
}
