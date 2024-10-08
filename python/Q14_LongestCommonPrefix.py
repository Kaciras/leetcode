class Solution:
	"""
	min() 函数中 key 的使用
	enumerate() 用来同时遍历索引和元素
	"""

	def longestCommonPrefix(self, strs: list[str]) -> str:
		if not strs:
			return ""
		shortest = min(strs, key=len)
		for i, ch in enumerate(shortest):
			for s in strs:
				if ch != s[i]:
					return shortest[:i]
		return shortest


def test_example1():
	assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == "fl"


def test_example2():
	assert Solution().longestCommonPrefix(["a"]) == "a"


def test_example3():
	assert Solution().longestCommonPrefix(["dog", "racecar", "car"]) == ""


def test_case1():
	assert Solution().longestCommonPrefix([]) == ""


def test_case2():
	assert Solution().longestCommonPrefix(["aca", "cba"]) == ""
