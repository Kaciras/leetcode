import collections


class Solution:
	"""其实就是统计字符的个数"""

	def isAnagram(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: bool
		"""
		return collections.Counter(s) == collections.Counter(t)


if __name__ == '__main__':
	print(Solution().isAnagram("", ""))
	print(Solution().isAnagram("anagram", "nagaram"))
	print(Solution().isAnagram("rat", "car"))
