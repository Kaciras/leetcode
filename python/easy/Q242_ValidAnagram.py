import collections


class Solution:

	def isAnagram(self, s: str, t: str) -> bool:
		"""其实就是统计字符的个数"""
		return collections.Counter(s) == collections.Counter(t)


if __name__ == '__main__':
	print(Solution().isAnagram("", ""))
	print(Solution().isAnagram("anagram", "nagaram"))
	print(Solution().isAnagram("rat", "car"))
