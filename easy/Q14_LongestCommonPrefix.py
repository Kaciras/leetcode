class Solution:
	"""
	min() 函数中key的使用
	enumerate() 用来同时遍历索引和元素
	"""

	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if len(strs) == 0:
			return ""
		shortest = min(strs, key=len)
		for i, ch in enumerate(shortest):
			for s in strs:
				if ch != s[i]:
					return shortest[:i]
		return shortest


if __name__ == '__main__':
	print(Solution().longestCommonPrefix([]))
	print(Solution().longestCommonPrefix(["flower","flow","flight"]))
	print(Solution().longestCommonPrefix(["a"]))
	print(Solution().longestCommonPrefix(["aca","cba"]))