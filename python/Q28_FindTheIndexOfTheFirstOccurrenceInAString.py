from utils import benckmark


class Solution:
	"""
	KMP 算法，预先计算出匹配失败后模式串指针要跳回的位置，从而保证指针不回溯。
	当然，最佳实现是调用几乎所有语言都有的 indexOf() API。
	"""

	def strStr(self, haystack: str, needle: str) -> int:
		if len(needle) == 0:
			return 0
		if len(needle) > len(haystack):
			return -1

		next_, i, k = [0] * len(needle), 0, -1
		next_[0] = -1

		# 无论 AhoCorasick 还是 KMP 都是预处理模式串的。
		while i < len(needle) - 1:
			if needle[i] == needle[k] or k == -1:
				i += 1
				k += 1
				next_[i] = k
			else:
				k = next_[k]

		i = j = 0
		while i < len(haystack):
			if j == -1 or haystack[i] == needle[j]:
				i += 1
				j += 1
				if j == len(needle):
					return i - j
			else:
				j = next_[j]

		return -1


def test_example1():
	assert Solution().strStr("sadbutsad", "sad") == 0


def test_example2():
	assert Solution().strStr("leetcode", "leeto") == -1


def test_case1():
	assert Solution().strStr("ababcabcaeabababca", "abababca") == 10


def test_case2():
	assert Solution().strStr("mississippi", "issi") == 1


def test_user1():
	assert Solution().strStr("", "abc") == -1


if __name__ == '__main__':
	benckmark(Solution().strStr, "ababcabcaeabababca", "abababca", ratio=0.1)
