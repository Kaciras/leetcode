class Solution:

	def trailingZeroes(self, n: int) -> int:
		"""
		组成阶乘的数中共有多少对 2 和 5 的组合即可。
		又因为 5 的个数一定比 2 少，问题简化为计算 5 的个数
		"""
		d, zeros = 5, 0
		while n >= d:
			zeros += n // d
			d *= 5
		return zeros


if __name__ == '__main__':
	print(Solution().trailingZeroes(1000))
