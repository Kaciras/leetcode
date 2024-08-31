class Solution:
	def divide(self, dividend, divisor):
		"""
		:type dividend: int
		:type divisor: int
		:rtype: int
		"""
		negative, quotient = (dividend < 0) ^ (divisor < 0), 0
		dividend, divisor = abs(dividend), abs(divisor)

		while dividend >= divisor:
			dx, qx = divisor, 1

			# dx + dx < 0 判断溢出，虽然PY不会溢出
			while dx + dx < 0 or dx + dx < dividend:
				dx += dx
				qx += qx
			dividend -= dx
			quotient += qx

		return -quotient if negative else min(quotient, 2147483647)


if __name__ == '__main__':
	print(Solution().divide(0, -1))
	print(Solution().divide(1, 1))
	print(Solution().divide(100, 3))
	print(Solution().divide(50, -5))
	print(Solution().divide(2 ** 31, 2))
	print(Solution().divide(-2147483648, -1))
