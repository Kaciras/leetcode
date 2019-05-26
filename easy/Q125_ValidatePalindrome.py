from utils import benckmark


class Solution:

	def isPalindrome(self, s: str) -> bool:
		s = [c for c in s.lower() if c.isalnum()]
		return s == s[::-1]


if __name__ == '__main__':
	print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
	print(Solution().isPalindrome("race a car"))

	benckmark(Solution().isPalindrome, "A man, a plan, a canal: Panama")
