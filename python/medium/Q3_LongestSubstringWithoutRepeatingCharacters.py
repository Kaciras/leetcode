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


if __name__ == '__main__':
	assert Solution().lengthOfLongestSubstring("") == 0
	assert Solution().lengthOfLongestSubstring(" ") == 1
	assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
	assert Solution().lengthOfLongestSubstring("bbbbb") == 1
	assert Solution().lengthOfLongestSubstring("pwwkew") == 3
	assert Solution().lengthOfLongestSubstring("abba") == 2
