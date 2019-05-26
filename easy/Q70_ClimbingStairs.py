class Solution:

	def climbStairs(self, n: int) -> int:
		if n < 2:
			return n

		a, b, = 1, 2
		while n > 2:
			a, b = b, a + b
			n -= 1
		return b

if __name__ == '__main__':
	print(Solution().climbStairs(2))
	print(Solution().climbStairs(3))
	print(Solution().climbStairs(35))