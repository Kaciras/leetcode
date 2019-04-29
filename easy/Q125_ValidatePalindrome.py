import string


class Solution:
	"""用filter()直接替换更方便"""

	def isPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		ls = string.ascii_lowercase + string.digits
		s = [c for c in s.lower() if c.isalnum()]
		return s == s[::-1]

if __name__ == '__main__':
	print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
	print(Solution().isPalindrome("race a car"))
