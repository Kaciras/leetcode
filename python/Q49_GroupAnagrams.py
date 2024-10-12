from pytest_unordered import unordered


class Solution:

	def groupAnagrams(self, strs: list[str]):
		"""
		直接排序，由相同字母组成的词一定会排成一样的。
		"""
		dictionary = {}
		for x in strs:
			sorted_x = "".join(sorted(x))
			if sorted_x in dictionary:
				dictionary[sorted_x].append(x)
			else:
				dictionary[sorted_x] = [x]

		return list(dictionary.values())


def test_example1():
	assert Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == unordered([
		unordered(["bat"]),
		unordered(["nat", "tan"]),
		unordered(["ate", "eat", "tea"]),
	])


def test_example2():
	assert Solution().groupAnagrams([""]) == [[""]]


def test_example3():
	assert Solution().groupAnagrams(["a"]) == [["a"]]
