from typing import List


class Solution:

	def reverseString(self, s: List[str]) -> None:
		s.reverse()  # 标准库的API有这个方法
		# s[::] = s[::-1] # Python 自带的语法也能直接搞定

	def reverseString2(self, s: List[str]) -> None:
		i, j = 0, len(s) - 1
		while i < j:
			s[i], s[j] = s[j], s[i]
			i, j = i + 1, j - 1


if __name__ == '__main__':
	a = ["1", "2", "3", "4", "5"]
	Solution().reverseString2(a)
	print(a)

	a = ["1", "2", "3", "4", "5", "6"]
	Solution().reverseString2(a)
	print(a)
