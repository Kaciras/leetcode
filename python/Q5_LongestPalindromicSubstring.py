class Solution:
	"""另一种更好的办法是使用切片来比较，并跳过比最长短的"""

	def longestPalindrome(self, s: str) -> str:
		"""
		中心比较法，遍历字符，假定该字符是中心并检查两侧是否相等。
		"""

		def palindrome(j, k):
			while j >= 0 and k < len(s) and s[j] == s[k]:
				j -= 1
				k += 1
			return s[j + 1:k]

		result = ""
		for i in range(len(s)):
			even = palindrome(i, i + 1)
			odd = palindrome(i, i)
			result = max(result, odd, even, key=len)

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
