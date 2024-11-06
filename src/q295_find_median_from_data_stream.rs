use std::collections::BinaryHeap;

struct MedianFinder {
	min: BinaryHeap<i32>,
	max: BinaryHeap<i32>,
}

// 两个二分堆，分别大小顶，这样就能组合出中顶的堆。
impl MedianFinder {

	fn new() -> Self {
		return MedianFinder { min: BinaryHeap::new(), max: BinaryHeap::new() };
	}

	fn add_num(&mut self, num: i32) {
		self.max.push(num);
		self.min.push(-self.max.pop().unwrap());
		if self.min.len() > self.max.len() {
			self.max.push(-self.min.pop().unwrap());
		}
	}

	fn find_median(&self) -> f64 {
		let hi = *self.max.peek().unwrap() as f64;
		if self.min.len() < self.max.len() {
			return hi;
		}
		let lo = *self.min.peek().unwrap() as f64;
		return (-lo + hi) / 2.0;
	}
}

#[cfg(test)]
mod tests {
	use super::*;

	#[test]
	fn example1() {
		let mut instance = MedianFinder::new();
		instance.add_num(1);
		instance.add_num(2);
		assert_eq!(instance.find_median(), 1.5);
		instance.add_num(3);
		assert_eq!(instance.find_median(), 2.0);
	}
}
