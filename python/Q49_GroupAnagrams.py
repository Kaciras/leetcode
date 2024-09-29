from utils import print_martix


class Solution:

	def groupAnagrams(self, strs: list[str]):
		"""
		直接排序，由相同字母组成的词一定会排成一样的。
		注意 1：sorted 直接排序更方便
		"""
		dic = {}
		for x in strs:
			sorted_x = "".join(sorted(x))
			if sorted_x in dic:
				dic[sorted_x].append(x)
			else:
				dic[sorted_x] = [x]

		return list(dic.values())

	def groupAnagrams2(self, strs: list[str]):
		def str_sort(s):
			r = list(s)
			r.sort()
			return "".join(r), s

		b = list(map(str_sort, strs))
		b.sort(key=lambda x: x[0])
		result = []

		p = c = None
		for s in b:
			if s[0] != p:
				c = []
				result.append(c)
				p = s[0]
			c.append(s[1])
		return result


if __name__ == '__main__':
	print_martix(Solution().groupAnagrams([]))
	print_martix(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
