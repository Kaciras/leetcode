from utils import benckmark


class Solution:
	"""while循环改成for，耗时降低了1.2秒/百万次"""

	def climbStairs(self, n: int) -> int:
		if n < 2:
			return n
		a, b, = 1, 2
		for _ in range(n - 2):
			a, b = b, a + b
		return b


if __name__ == '__main__':
	print(Solution().climbStairs(2))
	print(Solution().climbStairs(3))
	print(Solution().climbStairs(35))
	benckmark(Solution().climbStairs, 35)
