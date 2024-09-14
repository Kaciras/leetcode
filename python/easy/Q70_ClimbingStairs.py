from utils import benckmark


class Solution:
	"""while 循环改成 for，耗时降低了 1.2秒/百万次"""

	def climbStairs(self, n: int) -> int:
		if n < 2:
			return n
		# 上第一次和第二层的走法数量
		a, b = 1, 2
		# 从第二层开始递归
		for _ in range(n - 2):
			# 接下来是第二层和第三层，以此类推……
			a, b = b, a + b
		return b


if __name__ == '__main__':
	print(Solution().climbStairs(2))
	print(Solution().climbStairs(3))
	print(Solution().climbStairs(35))
	benckmark(Solution().climbStairs, 35)
