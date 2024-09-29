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


if __name__ == '__main__':
	print(Solution().longestPalindrome("bb"))
	print(Solution().longestPalindrome("ccc"))
	print(Solution().longestPalindrome("a"))
	print(Solution().longestPalindrome(""))
	print(Solution().longestPalindrome("babad")) # bab
	print(Solution().longestPalindrome("cbbd")) # bb
