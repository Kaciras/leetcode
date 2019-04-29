class Solution:

	def countAndSay(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		s, x = "1", ""
		for _ in range(n - 1):
			v, count = s[0], 0
			for ch in s:
				if ch != v:
					x += str(count) + v
					v = ch
					count = 0
				count += 1
			s, x = x + str(count) + v, ""
		return s


if __name__ == '__main__':
	for ii in range(1, 30):
		print(Solution().countAndSay(ii))
