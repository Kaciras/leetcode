class Solution:

	def lengthOfLongestSubstring(self, s: str) -> int:
		"""
		要记录不同元素的位置，一个 Map 是必要的。
		遍历每个元素，记录下每个字最后出现的位置，再出现时即字串结束。
		"""
		left, longest, last = 0, 0, {}

		for i, char in enumerate(s):
			j = last.get(char)
			if j is not None and j >= left:
				if i - left > longest:
					longest = i - left
				left = j + 1
			last[char] = i

		return max(longest, len(s) - left)


def test_case1():
	assert Solution().lengthOfLongestSubstring("abba") == 2


def test_example1():
	assert Solution().lengthOfLongestSubstring("abcabcbb") == 3


def test_example2():
	assert Solution().lengthOfLongestSubstring("bbbbb") == 1


def test_example3():
	assert Solution().lengthOfLongestSubstring("pwwkew") == 3


def test_user1():
	assert Solution().lengthOfLongestSubstring("") == 0
