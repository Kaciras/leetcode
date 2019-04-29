class Solution:
	"""KMP 算法"""

	def strStr(self, haystack, needle):
		"""
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		if len(needle) == 0:
			return 0
		if len(needle) > len(haystack):
			return -1

		next_, i, k = [0] * len(needle), 0, -1
		next_[0] = -1

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


if __name__ == '__main__':
	print(Solution().strStr("ababcabcaeabababca", "abababca"))
	print(Solution().strStr("mississippi", "issi"))
	print(Solution().strStr("hello", ""))
	print(Solution().strStr("", "abc"))
	print(Solution().strStr("hello", "ll"))
	print(Solution().strStr("aaaaa", "bba"))