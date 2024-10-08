class Solution:
	"""另一种更好的办法是使用切片来比较，并跳过比最长短的"""

	def longestPalindrome(self, s: str) -> str:
		def palindrome(j, k):
			while j >= 0 and k < len(s) and s[j] == s[k]:
				j -= 1
				k += 1
			return s[j + 1:k]

		result = ""
		for i in range(len(s)):
			result = max(result, palindrome(i, i), palindrome(i, i + 1), key=len)

		return result


def test_example1():
	assert Solution().longestPalindrome("babad") == "bab"


def test_example2():
	assert Solution().longestPalindrome("cbbd") == "bb"


def test_case1():
	assert Solution().longestPalindrome("") == ""


def test_case2():
	assert Solution().longestPalindrome("a") == "a"


def test_case3():
	assert Solution().longestPalindrome("bb") == "bb"
