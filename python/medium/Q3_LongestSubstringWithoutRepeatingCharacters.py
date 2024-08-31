class Solution:

	def lengthOfLongestSubstring(self, s: str) -> int:
		last = {}
		left = longest = 0

		for i, char in enumerate(s):
			if (char in last) and (last[char] >= left):
				if i - left > longest:
					longest = i - left
				left = last[char] + 1
			last[char] = i

		if len(s) - left > longest:
			return len(s) - left

		return longest

	def lengthOfLongestSubstring2(self, s: str) -> int:
		result, current, set_ = 0, [], set()

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
			result = max(result, len(current))

		return result


if __name__ == '__main__':
	print(Solution().lengthOfLongestSubstring(""))
	print(Solution().lengthOfLongestSubstring("abcabcbb"))  # 3
	print(Solution().lengthOfLongestSubstring("bbbbb"))  # 1
	print(Solution().lengthOfLongestSubstring("pwwkew"))  # 3
