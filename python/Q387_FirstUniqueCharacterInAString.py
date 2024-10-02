import string


class Solution:

	def firstUniqChar(self, s: str) -> int:
		lowercase = string.ascii_lowercase
		i = [s.index(label) for label in lowercase if s.count(label) == 1]
		return min(i) if len(i) else -1

	def firstUniqChar_1(self, s: str) -> int:
		d, r, f = {}, float("inf"), False
		for i in range(len(s)):
			ch = s[i]
			if not d.__contains__(ch):
				d[ch] = [0, i]
			d[ch][0] += 1
		for x in d.values():
			if x[0] == 1:
				r, f = min(r, x[1]), True
		return r if f else -1


if __name__ == '__main__':
	print(Solution().firstUniqChar("leetcode"))
	print(Solution().firstUniqChar("loveleetcode"))
