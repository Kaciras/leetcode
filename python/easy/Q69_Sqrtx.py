class Solution:
	def mySqrt(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		if x == 0:
			return 0
		eps = 1e-12
		t = x
		while abs(t - x / t) > eps * t:
			t = (t + x / t) / 2
		return int(t)


if __name__ == '__main__':
	print(Solution().mySqrt(0))
	print(Solution().mySqrt(2))
	print(Solution().mySqrt(8))
	print(Solution().mySqrt(1024))
	print(Solution().mySqrt(2147395599))