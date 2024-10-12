class Solution:

	def countAndSay(self, n: int) -> str:
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


def test_example1():
	assert Solution().countAndSay(4) == "1211"


def test_example2():
	assert Solution().countAndSay(1) == "1"


# 想起小时候看的一本左逼环保小说了，里头这玩意还挺有意思的。
if __name__ == '__main__':
	for ii in range(1, 30):
		print(Solution().countAndSay(ii) + "\n")
