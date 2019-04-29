class Solution:

	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		left = longest= 0
		last = dict()

		for i, char in enumerate(s):
			if (char in last) and (last[char] >= left):
				if i - left > longest:
					longest = i - left
				left = last[char] + 1
			last[char] = i

		if len(s) - left > longest:
			return len(s) - left
		return longest

	def lengthOfLongestSubstring2(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		r, current, set_ = 0, [], set()
		for ch in s:
			if ch in set_:
				while True:
					d = current[0]
					set_.remove(d)
					del current[0]
					if d == ch:
						break
			set_.add(ch)
			current.append(ch)
			r = max(r, len(current))
		return r


if __name__ == '__main__':
	print(Solution().lengthOfLongestSubstring([]))
	print(Solution().lengthOfLongestSubstring("abcabcbb"))
	print(Solution().lengthOfLongestSubstring("bbbbb"))
	print(Solution().lengthOfLongestSubstring("pwwkew"))